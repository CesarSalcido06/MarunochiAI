"""
Filesystem watcher for incremental codebase indexing.

Monitors code files for changes and automatically updates indices in real-time.
Target: <100ms per file change (parse + chunk + index).
"""

import asyncio
import time
from pathlib import Path
from typing import Set, Optional, Callable
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent, FileCreatedEvent, FileDeletedEvent
from loguru import logger

from .parser import CodeParser
from .chunker import CodeChunker
from .indexer import CodebaseIndexer
from .keyword_indexer import KeywordIndexer


class CodebaseWatcher:
    """
    Watch filesystem for code changes and update indices incrementally.

    Features:
    - Real-time file change detection
    - Automatic re-parsing and re-indexing
    - Sub-100ms update target
    - Smart filtering (skip .git, node_modules, etc.)
    - Debouncing for rapid changes
    """

    # File extensions to watch
    CODE_EXTENSIONS = {'.py', '.js', '.ts', '.tsx', '.jsx'}

    # Directories to exclude
    EXCLUDED_DIRS = {
        '.venv', 'venv', '__pycache__', '.git', 'node_modules',
        '.pytest_cache', 'dist', 'build', '.mypy_cache', '.ruff_cache',
        'env', '.tox', 'htmlcov', '.coverage', '.eggs'
    }

    def __init__(
        self,
        codebase_path: str,
        vector_indexer: CodebaseIndexer,
        keyword_indexer: Optional[KeywordIndexer] = None,
        debounce_ms: int = 500,
        on_change: Optional[Callable] = None
    ):
        """
        Initialize codebase watcher.

        Args:
            codebase_path: Root directory to watch
            vector_indexer: ChromaDB indexer for vector search
            keyword_indexer: Optional SQLite FTS5 indexer
            debounce_ms: Milliseconds to wait before processing changes
            on_change: Optional callback when files are reindexed
        """
        self.codebase_path = Path(codebase_path).resolve()
        self.vector_indexer = vector_indexer
        self.keyword_indexer = keyword_indexer
        self.debounce_ms = debounce_ms
        self.on_change = on_change

        # Initialize components
        self.parser = CodeParser()
        self.chunker = CodeChunker()

        # Watchdog observer
        self.observer: Optional[Observer] = None
        self._running = False

        # Debouncing
        self._pending_changes: Set[Path] = set()
        self._debounce_task: Optional[asyncio.Task] = None
        self._debounce_lock = asyncio.Lock()

    def _should_watch(self, filepath: Path) -> bool:
        """
        Check if file should be watched.

        Args:
            filepath: File path to check

        Returns:
            True if file should be watched
        """
        # Check if file exists and is a file
        if not filepath.is_file():
            return False

        # Check extension
        if filepath.suffix not in self.CODE_EXTENSIONS:
            return False

        # Check for excluded directories
        try:
            relative_path = filepath.relative_to(self.codebase_path)
            if any(excluded in relative_path.parts for excluded in self.EXCLUDED_DIRS):
                return False
        except ValueError:
            # File is outside codebase_path
            return False

        return True

    async def start_watching(self) -> None:
        """
        Start watching the codebase for changes.

        This starts the watchdog observer in a background thread.
        """
        if self._running:
            logger.warning("Watcher already running")
            return

        self._running = True

        # Create event handler
        handler = CodeFileHandler(self)

        # Create and start observer
        self.observer = Observer()
        self.observer.schedule(handler, str(self.codebase_path), recursive=True)
        self.observer.start()

        logger.info(f"Started watching: {self.codebase_path}")
        logger.info(f"Watching extensions: {', '.join(self.CODE_EXTENSIONS)}")

    def stop_watching(self) -> None:
        """Stop watching the codebase."""
        if not self._running:
            return

        self._running = False

        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.observer = None

        logger.info("Stopped watching codebase")

    async def on_file_created(self, filepath: Path) -> None:
        """
        Handle new file creation.

        Args:
            filepath: Path to created file
        """
        if not self._should_watch(filepath):
            return

        logger.debug(f"File created: {filepath}")
        await self._schedule_reindex(filepath)

    async def on_file_modified(self, filepath: Path) -> None:
        """
        Handle file modification.

        Args:
            filepath: Path to modified file
        """
        if not self._should_watch(filepath):
            return

        logger.debug(f"File modified: {filepath}")
        await self._schedule_reindex(filepath)

    async def on_file_deleted(self, filepath: Path) -> None:
        """
        Handle file deletion.

        Args:
            filepath: Path to deleted file
        """
        # Note: File may not exist anymore, so we can't check _should_watch
        # Just check extension from the path
        if filepath.suffix not in self.CODE_EXTENSIONS:
            return

        logger.debug(f"File deleted: {filepath}")
        await self._delete_from_indices(filepath)

    async def _schedule_reindex(self, filepath: Path) -> None:
        """
        Schedule file for re-indexing with debouncing.

        Args:
            filepath: File to reindex
        """
        async with self._debounce_lock:
            self._pending_changes.add(filepath)

            # Cancel existing debounce task
            if self._debounce_task and not self._debounce_task.done():
                self._debounce_task.cancel()

            # Schedule new debounce task
            self._debounce_task = asyncio.create_task(self._debounce_and_process())

    async def _debounce_and_process(self) -> None:
        """
        Wait for debounce period then process pending changes.
        """
        await asyncio.sleep(self.debounce_ms / 1000.0)

        async with self._debounce_lock:
            if not self._pending_changes:
                return

            # Process all pending changes
            files_to_process = list(self._pending_changes)
            self._pending_changes.clear()

        logger.info(f"Processing {len(files_to_process)} file changes")

        for filepath in files_to_process:
            await self._reindex_file(filepath)

    async def _reindex_file(self, filepath: Path) -> None:
        """
        Re-parse, chunk, and index a single file.

        Target: <100ms total time.

        Args:
            filepath: File to reindex
        """
        start_time = time.time()

        try:
            # Delete old chunks from both indices
            filepath_str = str(filepath)
            await self.vector_indexer.delete_file(filepath_str)
            if self.keyword_indexer:
                await self.keyword_indexer.delete_file(filepath_str)

            # Parse file
            parsed = await self.parser.parse_file(filepath_str)
            if parsed is None:
                logger.warning(f"Failed to parse {filepath}")
                return

            # Chunk file
            chunks = await self.chunker.chunk_file(parsed)
            if not chunks:
                logger.warning(f"No chunks generated for {filepath}")
                return

            # Index in vector database
            indexed_vector = await self.vector_indexer._index_chunks_batch(chunks)

            # Index in keyword database
            indexed_keyword = 0
            if self.keyword_indexer:
                indexed_keyword = await self.keyword_indexer.index_chunks(chunks)

            duration_ms = int((time.time() - start_time) * 1000)

            logger.info(
                f"Reindexed {filepath.name}: {len(chunks)} chunks "
                f"({indexed_vector} vector, {indexed_keyword} keyword) in {duration_ms}ms"
            )

            # Call optional callback
            if self.on_change:
                await self.on_change(filepath, len(chunks), duration_ms)

        except Exception as e:
            duration_ms = int((time.time() - start_time) * 1000)
            logger.error(f"Failed to reindex {filepath} after {duration_ms}ms: {e}")

    async def _delete_from_indices(self, filepath: Path) -> None:
        """
        Delete file from all indices.

        Args:
            filepath: File to delete
        """
        try:
            filepath_str = str(filepath)

            # Delete from vector index
            await self.vector_indexer.delete_file(filepath_str)

            # Delete from keyword index
            if self.keyword_indexer:
                await self.keyword_indexer.delete_file(filepath_str)

            logger.info(f"Deleted {filepath.name} from indices")

            # Call optional callback
            if self.on_change:
                await self.on_change(filepath, 0, 0)

        except Exception as e:
            logger.error(f"Failed to delete {filepath}: {e}")


class CodeFileHandler(FileSystemEventHandler):
    """
    Watchdog event handler for code file changes.

    Delegates to CodebaseWatcher for actual processing.
    """

    def __init__(self, watcher: CodebaseWatcher):
        super().__init__()
        self.watcher = watcher

    def on_created(self, event):
        """Handle file creation."""
        if event.is_directory:
            return

        filepath = Path(event.src_path)
        asyncio.run(self.watcher.on_file_created(filepath))

    def on_modified(self, event):
        """Handle file modification."""
        if event.is_directory:
            return

        filepath = Path(event.src_path)
        asyncio.run(self.watcher.on_file_modified(filepath))

    def on_deleted(self, event):
        """Handle file deletion."""
        if event.is_directory:
            return

        filepath = Path(event.src_path)
        asyncio.run(self.watcher.on_file_deleted(filepath))
