"""BM25 keyword search using SQLite FTS5."""

import aiosqlite
from pathlib import Path
from typing import List, Tuple, Optional
from loguru import logger

from .models import CodeChunk


class KeywordIndexer:
    """
    BM25 keyword search using SQLite FTS5.

    Provides fast full-text search as complement to vector search.
    """

    def __init__(self, db_path: Optional[str] = None):
        """
        Initialize KeywordIndexer.

        Args:
            db_path: Path to SQLite database (default: ~/MarunochiAI/data/keyword_index.db)
        """
        self.db_path = db_path or str(
            Path.home() / "MarunochiAI" / "data" / "keyword_index.db"
        )

        # Create parent directory
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)

        self.db = None
        self._initialized = False

    async def _ensure_initialized(self) -> None:
        """Ensure database is initialized."""
        if self._initialized:
            return

        await self._init_db()
        self._initialized = True

    async def _init_db(self) -> None:
        """Initialize SQLite database with FTS5 schema."""
        try:
            self.db = await aiosqlite.connect(self.db_path)

            # Create FTS5 virtual table for full-text search
            # FTS5 automatically uses BM25 ranking
            await self.db.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS code_fts USING fts5(
                    chunk_id UNINDEXED,
                    content,
                    filepath UNINDEXED,
                    name,
                    language UNINDEXED,
                    chunk_type UNINDEXED,
                    tokenize='porter unicode61'
                )
            """)

            # Create metadata table for storing chunk info
            await self.db.execute("""
                CREATE TABLE IF NOT EXISTS chunk_metadata (
                    chunk_id TEXT PRIMARY KEY,
                    filepath TEXT,
                    name TEXT,
                    language TEXT,
                    chunk_type TEXT,
                    line_start INTEGER,
                    line_end INTEGER,
                    last_modified REAL
                )
            """)

            # Create index on filepath for fast deletion
            await self.db.execute("""
                CREATE INDEX IF NOT EXISTS idx_filepath
                ON chunk_metadata(filepath)
            """)

            await self.db.commit()
            logger.info(f"Initialized keyword index at {self.db_path}")

        except Exception as e:
            logger.error(f"Failed to initialize keyword index: {e}")
            raise

    async def index_chunk(self, chunk: CodeChunk) -> None:
        """
        Add a single chunk to the keyword index.

        Args:
            chunk: CodeChunk to index
        """
        await self._ensure_initialized()

        try:
            # Add to FTS5 table
            await self.db.execute("""
                INSERT INTO code_fts (chunk_id, content, filepath, name, language, chunk_type)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                chunk.id,
                chunk.content,
                chunk.filepath,
                chunk.name,
                chunk.language.value,
                chunk.chunk_type.value
            ))

            # Add to metadata table
            await self.db.execute("""
                INSERT OR REPLACE INTO chunk_metadata
                (chunk_id, filepath, name, language, chunk_type, line_start, line_end, last_modified)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                chunk.id,
                chunk.filepath,
                chunk.name,
                chunk.language.value,
                chunk.chunk_type.value,
                chunk.line_range[0],
                chunk.line_range[1],
                chunk.last_modified
            ))

            await self.db.commit()

        except Exception as e:
            logger.error(f"Failed to index chunk {chunk.id}: {e}")
            raise

    async def index_chunks(self, chunks: List[CodeChunk]) -> int:
        """
        Batch index multiple chunks.

        Args:
            chunks: List of CodeChunk objects

        Returns:
            Number of chunks indexed
        """
        await self._ensure_initialized()

        if not chunks:
            return 0

        try:
            # Batch insert into FTS5
            await self.db.executemany("""
                INSERT INTO code_fts (chunk_id, content, filepath, name, language, chunk_type)
                VALUES (?, ?, ?, ?, ?, ?)
            """, [
                (
                    chunk.id,
                    chunk.content,
                    chunk.filepath,
                    chunk.name,
                    chunk.language.value,
                    chunk.chunk_type.value
                )
                for chunk in chunks
            ])

            # Batch insert into metadata table
            await self.db.executemany("""
                INSERT OR REPLACE INTO chunk_metadata
                (chunk_id, filepath, name, language, chunk_type, line_start, line_end, last_modified)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, [
                (
                    chunk.id,
                    chunk.filepath,
                    chunk.name,
                    chunk.language.value,
                    chunk.chunk_type.value,
                    chunk.line_range[0],
                    chunk.line_range[1],
                    chunk.last_modified
                )
                for chunk in chunks
            ])

            await self.db.commit()
            logger.info(f"Indexed {len(chunks)} chunks in keyword index")
            return len(chunks)

        except Exception as e:
            logger.error(f"Failed to batch index chunks: {e}")
            return 0

    async def search(
        self,
        query: str,
        limit: int = 20,
        filter_language: Optional[str] = None
    ) -> List[Tuple[str, float]]:
        """
        BM25 keyword search.

        Args:
            query: Search query
            limit: Maximum results
            filter_language: Optional language filter (e.g., "python")

        Returns:
            List of (chunk_id, bm25_score) tuples, ordered by relevance
        """
        await self._ensure_initialized()

        try:
            # Build query
            # FTS5 MATCH syntax: use quotes for phrases, OR/AND for boolean
            # BM25 ranking is automatic with FTS5

            if filter_language:
                # Join with metadata table for filtering
                cursor = await self.db.execute("""
                    SELECT
                        fts.chunk_id,
                        fts.rank AS score
                    FROM code_fts fts
                    JOIN chunk_metadata meta ON fts.chunk_id = meta.chunk_id
                    WHERE code_fts MATCH ?
                    AND meta.language = ?
                    ORDER BY rank
                    LIMIT ?
                """, (query, filter_language, limit))
            else:
                cursor = await self.db.execute("""
                    SELECT chunk_id, rank AS score
                    FROM code_fts
                    WHERE code_fts MATCH ?
                    ORDER BY rank
                    LIMIT ?
                """, (query, limit))

            results = await cursor.fetchall()

            # Convert rank (negative BM25 score) to positive scores
            # FTS5 rank is negative (lower is better), convert to positive
            return [(chunk_id, -score) for chunk_id, score in results]

        except Exception as e:
            logger.error(f"Keyword search failed: {e}")
            return []

    async def delete_file(self, filepath: str) -> None:
        """
        Delete all chunks for a file.

        Args:
            filepath: Path to file
        """
        await self._ensure_initialized()

        try:
            # Get chunk IDs for this file
            cursor = await self.db.execute("""
                SELECT chunk_id FROM chunk_metadata
                WHERE filepath = ?
            """, (filepath,))

            chunk_ids = [row[0] for row in await cursor.fetchall()]

            if chunk_ids:
                # Delete from FTS5 table
                placeholders = ','.join('?' * len(chunk_ids))
                await self.db.execute(f"""
                    DELETE FROM code_fts
                    WHERE chunk_id IN ({placeholders})
                """, chunk_ids)

                # Delete from metadata table
                await self.db.execute("""
                    DELETE FROM chunk_metadata
                    WHERE filepath = ?
                """, (filepath,))

                await self.db.commit()
                logger.debug(f"Deleted {len(chunk_ids)} chunks for {filepath}")

        except Exception as e:
            logger.error(f"Failed to delete file {filepath}: {e}")

    async def clear_index(self) -> None:
        """Clear all indexed data."""
        await self._ensure_initialized()

        try:
            await self.db.execute("DELETE FROM code_fts")
            await self.db.execute("DELETE FROM chunk_metadata")
            await self.db.commit()
            logger.info("Cleared keyword index")

        except Exception as e:
            logger.error(f"Failed to clear index: {e}")

    async def get_stats(self) -> dict:
        """
        Get indexing statistics.

        Returns:
            {
                'total_chunks': int,
                'total_files': int,
            }
        """
        await self._ensure_initialized()

        try:
            # Count total chunks
            cursor = await self.db.execute("""
                SELECT COUNT(*) FROM chunk_metadata
            """)
            total_chunks = (await cursor.fetchone())[0]

            # Count unique files
            cursor = await self.db.execute("""
                SELECT COUNT(DISTINCT filepath) FROM chunk_metadata
            """)
            total_files = (await cursor.fetchone())[0]

            return {
                'total_chunks': total_chunks,
                'total_files': total_files,
            }

        except Exception as e:
            logger.error(f"Failed to get stats: {e}")
            return {
                'total_chunks': 0,
                'total_files': 0,
            }

    async def close(self) -> None:
        """Close database connection."""
        if self.db:
            await self.db.close()
            self.db = None
            self._initialized = False
