"""Semantic code indexing with ChromaDB."""

import asyncio
import time
from pathlib import Path
from typing import Dict, List, Optional
from loguru import logger
import chromadb
from chromadb.config import Settings

from .models import CodeChunk, SearchResult, Language
from .parser import CodeParser
from .chunker import CodeChunker


class CodebaseIndexer:
    """
    Semantic code indexing with ChromaDB.

    Uses optimized HNSW settings from BenchAI for best performance.
    """

    def __init__(
        self,
        collection_name: str = "marunochithe_codebase",
        persist_directory: Optional[str] = None
    ):
        """
        Initialize CodebaseIndexer.

        Args:
            collection_name: Name for the ChromaDB collection
            persist_directory: Directory to persist the database (default: ~/MarunochiAI/data/chroma)
        """
        self.collection_name = collection_name
        self.persist_directory = persist_directory or str(
            Path.home() / "MarunochiAI" / "data" / "chroma"
        )

        # Initialize components
        self.parser = CodeParser()
        self.chunker = CodeChunker()

        # Initialize ChromaDB client
        self._init_chroma()

    def _init_chroma(self) -> None:
        """Initialize ChromaDB with optimized settings."""
        try:
            # Create persist directory
            Path(self.persist_directory).mkdir(parents=True, exist_ok=True)

            # Initialize persistent client
            self.client = chromadb.PersistentClient(
                path=self.persist_directory,
                settings=Settings(
                    anonymized_telemetry=False,
                    allow_reset=True,
                )
            )

            # Get or create collection with optimized HNSW settings
            # These settings are from BenchAI's optimized configuration
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={
                    "hnsw:space": "cosine",           # Cosine similarity
                    "hnsw:construction_ef": 200,      # Higher = better quality index
                    "hnsw:M": 32,                     # Max edges per node
                    "hnsw:search_ef": 100,            # Search accuracy
                    "hnsw:batch_size": 10000,         # Batch insert size
                }
            )

            logger.info(f"Initialized ChromaDB collection: {self.collection_name}")
            logger.info(f"Persist directory: {self.persist_directory}")

        except Exception as e:
            logger.error(f"Failed to initialize ChromaDB: {e}")
            raise

    async def index_codebase(
        self,
        codebase_path: str,
        file_extensions: Optional[List[str]] = None
    ) -> Dict:
        """
        Index entire codebase.

        Process:
        1. Find all code files
        2. Parse each file with CodeParser
        3. Chunk files hierarchically with CodeChunker
        4. Generate embeddings (ChromaDB handles this)
        5. Batch insert to ChromaDB

        Args:
            codebase_path: Path to codebase root
            file_extensions: File extensions to index (default: .py, .js, .ts, .tsx, .jsx)

        Returns:
            {
                'total_files': int,
                'total_chunks': int,
                'indexed_chunks': int,
                'duration_ms': int,
            }
        """
        start_time = time.time()

        # Default file extensions
        if file_extensions is None:
            file_extensions = ['.py', '.js', '.ts', '.tsx', '.jsx']

        # Find all code files
        code_files = self._find_code_files(codebase_path, file_extensions)
        logger.info(f"Found {len(code_files)} code files in {codebase_path}")

        # Parse and chunk all files
        all_chunks: List[CodeChunk] = []
        successful_files = 0

        for filepath in code_files:
            try:
                # Parse file
                parsed = await self.parser.parse_file_cached(str(filepath))
                if parsed is None:
                    continue

                # Chunk file
                chunks = await self.chunker.chunk_file(parsed)
                all_chunks.extend(chunks)
                successful_files += 1

            except Exception as e:
                logger.warning(f"Failed to process {filepath}: {e}")
                continue

        logger.info(f"Successfully parsed {successful_files}/{len(code_files)} files")
        logger.info(f"Generated {len(all_chunks)} total chunks")

        # Index chunks in ChromaDB
        indexed = await self._index_chunks_batch(all_chunks)

        duration_ms = int((time.time() - start_time) * 1000)

        return {
            'total_files': len(code_files),
            'successful_files': successful_files,
            'total_chunks': len(all_chunks),
            'indexed_chunks': indexed,
            'duration_ms': duration_ms,
        }

    async def index_file(self, filepath: str) -> Dict:
        """
        Index a single file (for incremental updates).

        Args:
            filepath: Path to file

        Returns:
            {
                'filepath': str,
                'chunks_added': int,
                'duration_ms': int,
            }
        """
        start_time = time.time()

        try:
            # Delete existing chunks for this file
            await self.delete_file(filepath)

            # Parse file
            parsed = await self.parser.parse_file(filepath)
            if parsed is None:
                return {
                    'filepath': filepath,
                    'chunks_added': 0,
                    'duration_ms': 0,
                    'error': 'Failed to parse file'
                }

            # Chunk file
            chunks = await self.chunker.chunk_file(parsed)

            # Index chunks
            indexed = await self._index_chunks_batch(chunks)

            duration_ms = int((time.time() - start_time) * 1000)

            return {
                'filepath': filepath,
                'chunks_added': indexed,
                'duration_ms': duration_ms,
            }

        except Exception as e:
            logger.error(f"Failed to index file {filepath}: {e}")
            return {
                'filepath': filepath,
                'chunks_added': 0,
                'duration_ms': int((time.time() - start_time) * 1000),
                'error': str(e)
            }

    async def delete_file(self, filepath: str) -> None:
        """
        Remove all chunks for a file from the index.

        Args:
            filepath: Path to file
        """
        try:
            # Query for chunks with this filepath
            results = self.collection.get(
                where={"filepath": filepath}
            )

            if results and results['ids']:
                # Delete chunks
                self.collection.delete(ids=results['ids'])
                logger.debug(f"Deleted {len(results['ids'])} chunks for {filepath}")

        except Exception as e:
            logger.warning(f"Failed to delete file {filepath}: {e}")

    async def search(
        self,
        query: str,
        limit: int = 5,
        filter_metadata: Optional[Dict] = None
    ) -> List[SearchResult]:
        """
        Semantic vector search.

        Args:
            query: Natural language or code query
            limit: Max results (default 5)
            filter_metadata: Filter by language, filepath, etc.
                Examples:
                - {"language": "python"}
                - {"filepath": {"$contains": "/src/"}}

        Returns:
            List of SearchResult with similarity scores
        """
        try:
            # Query ChromaDB
            results = self.collection.query(
                query_texts=[query],
                n_results=limit,
                where=filter_metadata,
                include=['metadatas', 'documents', 'distances']
            )

            # Convert to SearchResult objects
            search_results = []

            if results and results['ids'] and len(results['ids']) > 0:
                ids = results['ids'][0]
                metadatas = results['metadatas'][0]
                documents = results['documents'][0]
                distances = results['distances'][0]

                for i, chunk_id in enumerate(ids):
                    metadata = metadatas[i]
                    content = documents[i]
                    distance = distances[i]

                    # Convert distance to similarity score (0-1, higher is better)
                    # ChromaDB uses cosine distance, so similarity = 1 - distance
                    similarity = 1.0 - distance

                    search_results.append(SearchResult(
                        chunk_id=chunk_id,
                        filepath=metadata.get('filepath', ''),
                        name=metadata.get('name', ''),
                        content=content,
                        language=Language(metadata.get('language', 'unknown')),
                        chunk_type=metadata.get('chunk_type', 'file'),
                        line_range=(
                            metadata.get('line_start', 0),
                            metadata.get('line_end', 0)
                        ),
                        similarity=similarity,
                    ))

            return search_results

        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

    async def get_stats(self) -> Dict:
        """
        Get indexing statistics.

        Returns:
            {
                'total_chunks': int,
                'languages': {'python': 150, 'javascript': 80},
                'chunk_types': {'file': 100, 'class': 50, 'method': 200},
                'total_files': int,
            }
        """
        try:
            # Get all chunks
            results = self.collection.get(
                include=['metadatas']
            )

            total_chunks = len(results['ids'])

            # Count by language
            languages = {}
            chunk_types = {}
            filepaths = set()

            for metadata in results['metadatas']:
                # Count languages
                lang = metadata.get('language', 'unknown')
                languages[lang] = languages.get(lang, 0) + 1

                # Count chunk types
                chunk_type = metadata.get('chunk_type', 'unknown')
                chunk_types[chunk_type] = chunk_types.get(chunk_type, 0) + 1

                # Collect unique filepaths
                filepath = metadata.get('filepath', '')
                if filepath:
                    filepaths.add(filepath)

            return {
                'total_chunks': total_chunks,
                'total_files': len(filepaths),
                'languages': languages,
                'chunk_types': chunk_types,
            }

        except Exception as e:
            logger.error(f"Failed to get stats: {e}")
            return {
                'total_chunks': 0,
                'total_files': 0,
                'languages': {},
                'chunk_types': {},
            }

    async def clear_index(self) -> None:
        """Clear all indexed data."""
        try:
            self.client.delete_collection(name=self.collection_name)
            logger.info(f"Deleted collection: {self.collection_name}")

            # Recreate collection
            self._init_chroma()

        except Exception as e:
            logger.error(f"Failed to clear index: {e}")

    # === Private Methods ===

    def _find_code_files(
        self,
        path: str,
        extensions: List[str]
    ) -> List[Path]:
        """
        Find all code files in directory.

        Args:
            path: Directory path
            extensions: File extensions to include

        Returns:
            List of file paths
        """
        excluded_dirs = {
            '.venv', 'venv', '__pycache__', '.git', 'node_modules',
            '.pytest_cache', 'dist', 'build', '.mypy_cache', '.ruff_cache'
        }

        code_files = []
        root_path = Path(path)

        for file_path in root_path.rglob('*'):
            # Skip directories
            if not file_path.is_file():
                continue

            # Skip excluded directories
            if any(excluded in file_path.parts for excluded in excluded_dirs):
                continue

            # Check extension
            if file_path.suffix in extensions:
                code_files.append(file_path)

        return sorted(code_files)

    async def _index_chunks_batch(self, chunks: List[CodeChunk]) -> int:
        """
        Index chunks in batches for better performance.

        Args:
            chunks: List of CodeChunk objects

        Returns:
            Number of chunks indexed
        """
        if not chunks:
            return 0

        try:
            # Prepare batch data
            ids = []
            documents = []
            metadatas = []

            for chunk in chunks:
                ids.append(chunk.id)
                documents.append(chunk.content)

                # Metadata (ChromaDB stores as dict)
                metadatas.append({
                    'filepath': chunk.filepath,
                    'language': chunk.language.value,
                    'chunk_type': chunk.chunk_type.value,
                    'name': chunk.name,
                    'line_start': chunk.line_range[0],
                    'line_end': chunk.line_range[1],
                    'last_modified': chunk.last_modified,
                    'parent_id': chunk.parent_id or '',
                    'signature': chunk.signature or '',
                    'docstring': chunk.docstring or '',
                })

            # Add to ChromaDB (automatically generates embeddings)
            self.collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )

            logger.info(f"Indexed {len(chunks)} chunks")
            return len(chunks)

        except Exception as e:
            logger.error(f"Failed to index chunks: {e}")
            return 0
