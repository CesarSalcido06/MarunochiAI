"""
MarunochiAI Local Storage Module

SQLite-based storage for experiences, knowledge, and patterns.
Enables bidirectional sync with BenchAI orchestrator.
"""

import json
import uuid
import aiosqlite
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
from loguru import logger

from .config import get_settings


# Default storage path
DEFAULT_DB_PATH = Path.home() / "MarunochiAI" / "data" / "storage.db"


class StorageManager:
    """
    Manages local storage for A2A sync operations.

    Stores:
    - Experiences: Successful/failed task outcomes
    - Knowledge: Learned patterns and best practices
    - Patterns: Reusable code patterns
    """

    def __init__(self, db_path: Optional[Path] = None):
        """
        Initialize storage manager.

        Args:
            db_path: Path to SQLite database. Defaults to ~/MarunochiAI/data/storage.db
        """
        self.db_path = db_path or DEFAULT_DB_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialized = False

    async def initialize(self):
        """Create tables if they don't exist."""
        if self._initialized:
            return

        async with aiosqlite.connect(self.db_path) as db:
            # Experiences table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS experiences (
                    id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    category TEXT,
                    importance INTEGER DEFAULT 3,
                    success INTEGER DEFAULT 1,
                    metadata TEXT,
                    source TEXT DEFAULT 'local',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    synced_at TEXT
                )
            """)

            # Knowledge table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS knowledge (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    tags TEXT,
                    source TEXT DEFAULT 'local',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    synced_at TEXT
                )
            """)

            # Patterns table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS patterns (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    language TEXT,
                    pattern_code TEXT NOT NULL,
                    description TEXT,
                    usage_count INTEGER DEFAULT 0,
                    source TEXT DEFAULT 'local',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    synced_at TEXT
                )
            """)

            # Create indexes for common queries
            await db.execute("CREATE INDEX IF NOT EXISTS idx_exp_category ON experiences(category)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_exp_importance ON experiences(importance)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_exp_created ON experiences(created_at)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_know_source ON knowledge(source)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_pattern_lang ON patterns(language)")

            await db.commit()

        self._initialized = True
        logger.info(f"[Storage] Initialized database at {self.db_path}")

    # ==================
    # Experience Methods
    # ==================

    async def store_experience(
        self,
        content: str,
        category: Optional[str] = None,
        importance: int = 3,
        success: bool = True,
        metadata: Optional[Dict[str, Any]] = None,
        source: str = "local",
        experience_id: Optional[str] = None
    ) -> str:
        """
        Store an experience.

        Args:
            content: Description of the experience
            category: Category (e.g., "refactoring", "debugging")
            importance: Importance score 1-5
            success: Whether the task succeeded
            metadata: Additional metadata
            source: Origin ("local" or agent ID)
            experience_id: Optional ID (generates UUID if not provided)

        Returns:
            Experience ID
        """
        await self.initialize()

        exp_id = experience_id or f"exp-{uuid.uuid4().hex[:12]}"

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT OR REPLACE INTO experiences
                (id, content, category, importance, success, metadata, source, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    exp_id,
                    content,
                    category,
                    importance,
                    1 if success else 0,
                    json.dumps(metadata) if metadata else None,
                    source,
                    datetime.utcnow().isoformat()
                )
            )
            await db.commit()

        logger.debug(f"[Storage] Stored experience: {exp_id}")
        return exp_id

    async def get_experiences(
        self,
        limit: int = 50,
        category: Optional[str] = None,
        min_importance: int = 1,
        since: Optional[str] = None,
        source: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve experiences.

        Args:
            limit: Maximum number to return
            category: Filter by category
            min_importance: Minimum importance score
            since: ISO timestamp to filter by
            source: Filter by source

        Returns:
            List of experience dicts
        """
        await self.initialize()

        query = "SELECT * FROM experiences WHERE importance >= ?"
        params: List[Any] = [min_importance]

        if category:
            query += " AND category = ?"
            params.append(category)

        if since:
            query += " AND created_at > ?"
            params.append(since)

        if source:
            query += " AND source = ?"
            params.append(source)

        query += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(query, params) as cursor:
                rows = await cursor.fetchall()

        return [
            {
                "id": row["id"],
                "content": row["content"],
                "category": row["category"],
                "importance": row["importance"],
                "success": bool(row["success"]),
                "metadata": json.loads(row["metadata"]) if row["metadata"] else None,
                "source": row["source"],
                "created_at": row["created_at"]
            }
            for row in rows
        ]

    # ==================
    # Knowledge Methods
    # ==================

    async def store_knowledge(
        self,
        title: str,
        content: str,
        tags: Optional[List[str]] = None,
        source: str = "local",
        knowledge_id: Optional[str] = None
    ) -> str:
        """
        Store a knowledge note.

        Args:
            title: Note title
            content: Note content
            tags: List of tags
            source: Origin ("local" or agent ID)
            knowledge_id: Optional ID

        Returns:
            Knowledge ID
        """
        await self.initialize()

        know_id = knowledge_id or f"know-{uuid.uuid4().hex[:12]}"

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT OR REPLACE INTO knowledge
                (id, title, content, tags, source, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    know_id,
                    title,
                    content,
                    json.dumps(tags) if tags else None,
                    source,
                    datetime.utcnow().isoformat()
                )
            )
            await db.commit()

        logger.debug(f"[Storage] Stored knowledge: {know_id}")
        return know_id

    async def get_knowledge(
        self,
        limit: int = 50,
        since: Optional[str] = None,
        source: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve knowledge notes.

        Args:
            limit: Maximum number to return
            since: ISO timestamp to filter by
            source: Filter by source

        Returns:
            List of knowledge dicts
        """
        await self.initialize()

        query = "SELECT * FROM knowledge WHERE 1=1"
        params: List[Any] = []

        if since:
            query += " AND created_at > ?"
            params.append(since)

        if source:
            query += " AND source = ?"
            params.append(source)

        query += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(query, params) as cursor:
                rows = await cursor.fetchall()

        return [
            {
                "id": row["id"],
                "title": row["title"],
                "content": row["content"],
                "tags": json.loads(row["tags"]) if row["tags"] else [],
                "source": row["source"],
                "created_at": row["created_at"]
            }
            for row in rows
        ]

    # ==================
    # Pattern Methods
    # ==================

    async def store_pattern(
        self,
        name: str,
        pattern_code: str,
        language: Optional[str] = None,
        description: Optional[str] = None,
        source: str = "local",
        pattern_id: Optional[str] = None
    ) -> str:
        """
        Store a code pattern.

        Args:
            name: Pattern name
            pattern_code: The code pattern
            language: Programming language
            description: Pattern description
            source: Origin ("local" or agent ID)
            pattern_id: Optional ID

        Returns:
            Pattern ID
        """
        await self.initialize()

        pat_id = pattern_id or f"pat-{uuid.uuid4().hex[:12]}"

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT OR REPLACE INTO patterns
                (id, name, pattern_code, language, description, source, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    pat_id,
                    name,
                    pattern_code,
                    language,
                    description,
                    source,
                    datetime.utcnow().isoformat()
                )
            )
            await db.commit()

        logger.debug(f"[Storage] Stored pattern: {pat_id}")
        return pat_id

    async def get_patterns(
        self,
        limit: int = 50,
        language: Optional[str] = None,
        source: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve patterns.

        Args:
            limit: Maximum number to return
            language: Filter by language
            source: Filter by source

        Returns:
            List of pattern dicts
        """
        await self.initialize()

        query = "SELECT * FROM patterns WHERE 1=1"
        params: List[Any] = []

        if language:
            query += " AND language = ?"
            params.append(language)

        if source:
            query += " AND source = ?"
            params.append(source)

        query += " ORDER BY usage_count DESC, created_at DESC LIMIT ?"
        params.append(limit)

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(query, params) as cursor:
                rows = await cursor.fetchall()

        return [
            {
                "id": row["id"],
                "name": row["name"],
                "pattern_code": row["pattern_code"],
                "language": row["language"],
                "description": row["description"],
                "usage_count": row["usage_count"],
                "source": row["source"],
                "created_at": row["created_at"]
            }
            for row in rows
        ]

    async def increment_pattern_usage(self, pattern_id: str):
        """Increment usage count for a pattern."""
        await self.initialize()

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "UPDATE patterns SET usage_count = usage_count + 1 WHERE id = ?",
                (pattern_id,)
            )
            await db.commit()

    # ==================
    # Bulk Operations
    # ==================

    async def bulk_store(
        self,
        sync_type: str,
        items: List[Dict[str, Any]],
        source: str
    ) -> int:
        """
        Bulk store items from sync operation.

        Args:
            sync_type: "experience", "knowledge", or "pattern"
            items: List of items to store
            source: Source agent ID

        Returns:
            Number of items stored
        """
        count = 0

        for item in items:
            try:
                if sync_type == "experience":
                    await self.store_experience(
                        content=item.get("content", ""),
                        category=item.get("category"),
                        importance=item.get("importance", 3),
                        success=item.get("success", True),
                        metadata=item.get("metadata"),
                        source=source,
                        experience_id=item.get("id")
                    )
                    count += 1

                elif sync_type == "knowledge":
                    await self.store_knowledge(
                        title=item.get("title", "Untitled"),
                        content=item.get("content", ""),
                        tags=item.get("tags"),
                        source=source,
                        knowledge_id=item.get("id")
                    )
                    count += 1

                elif sync_type == "pattern":
                    await self.store_pattern(
                        name=item.get("name", item.get("pattern_name", "Unnamed")),
                        pattern_code=item.get("pattern_code", item.get("code", "")),
                        language=item.get("language"),
                        description=item.get("description"),
                        source=source,
                        pattern_id=item.get("id")
                    )
                    count += 1

            except Exception as e:
                logger.error(f"[Storage] Failed to store {sync_type} item: {e}")
                continue

        logger.info(f"[Storage] Bulk stored {count}/{len(items)} {sync_type} items from {source}")
        return count

    async def get_for_sync(
        self,
        sync_type: str,
        limit: int = 50,
        since: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get items for sync operation.

        Args:
            sync_type: "experience", "knowledge", or "pattern"
            limit: Maximum items to return
            since: Only items after this timestamp

        Returns:
            List of items for sync
        """
        if sync_type == "experience":
            return await self.get_experiences(limit=limit, since=since, source="local")
        elif sync_type == "knowledge":
            return await self.get_knowledge(limit=limit, since=since, source="local")
        elif sync_type == "pattern":
            return await self.get_patterns(limit=limit, source="local")
        else:
            return []

    # ==================
    # Stats
    # ==================

    async def get_stats(self) -> Dict[str, Any]:
        """Get storage statistics."""
        await self.initialize()

        async with aiosqlite.connect(self.db_path) as db:
            stats = {}

            # Experience stats
            async with db.execute("SELECT COUNT(*) FROM experiences") as cursor:
                row = await cursor.fetchone()
                stats["experiences_count"] = row[0] if row else 0

            async with db.execute("SELECT COUNT(*) FROM experiences WHERE source = 'local'") as cursor:
                row = await cursor.fetchone()
                stats["experiences_local"] = row[0] if row else 0

            # Knowledge stats
            async with db.execute("SELECT COUNT(*) FROM knowledge") as cursor:
                row = await cursor.fetchone()
                stats["knowledge_count"] = row[0] if row else 0

            # Pattern stats
            async with db.execute("SELECT COUNT(*) FROM patterns") as cursor:
                row = await cursor.fetchone()
                stats["patterns_count"] = row[0] if row else 0

            stats["db_path"] = str(self.db_path)

        return stats


# Global storage instance
_storage: Optional[StorageManager] = None


def get_storage() -> StorageManager:
    """Get or create storage manager instance."""
    global _storage
    if _storage is None:
        _storage = StorageManager()
    return _storage


async def init_storage() -> StorageManager:
    """Initialize storage and return instance."""
    storage = get_storage()
    await storage.initialize()
    return storage
