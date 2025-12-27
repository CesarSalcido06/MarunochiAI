"""Hierarchical code chunking for semantic indexing."""

from pathlib import Path
from typing import List
from loguru import logger

from .models import CodeChunk, ParsedFile, ChunkType, Language


class CodeChunker:
    """AST-aware hierarchical code chunking."""

    # Chunk size targets (in characters) - based on research
    CHUNK_SIZES = {
        'file': 2048,      # File-level (imports + structure overview)
        'class': 1024,     # Class-level (class + methods context)
        'method': 512,     # Method-level (implementation details)
    }

    def __init__(
        self,
        file_chunk_size: int = 2048,
        class_chunk_size: int = 1024,
        method_chunk_size: int = 512
    ):
        """
        Initialize chunker with size parameters.

        Args:
            file_chunk_size: Target size for file-level chunks
            class_chunk_size: Target size for class-level chunks
            method_chunk_size: Target size for method-level chunks
        """
        self.CHUNK_SIZES['file'] = file_chunk_size
        self.CHUNK_SIZES['class'] = class_chunk_size
        self.CHUNK_SIZES['method'] = method_chunk_size

    async def chunk_file(self, parsed: ParsedFile) -> List[CodeChunk]:
        """
        Create hierarchical chunks from parsed AST.

        Creates 3-level hierarchy:
        - Level 1: File-level chunk (imports + top-level structure)
        - Level 2: Class-level chunks (each class with context)
        - Level 3: Method/function-level chunks (each with signature)

        Args:
            parsed: Parsed file structure

        Returns:
            List of CodeChunk objects
        """
        chunks = []

        try:
            # Get file modification time
            mtime = Path(parsed.filepath).stat().st_mtime

            # Level 1: File-level chunk
            file_chunk = self._create_file_chunk(parsed, mtime)
            chunks.append(file_chunk)

            # Level 2: Class-level chunks
            class_chunks = self._create_class_chunks(parsed, file_chunk.id, mtime)
            chunks.extend(class_chunks)

            # Level 3: Method/function-level chunks
            method_chunks = self._create_method_chunks(parsed, file_chunk.id, mtime)
            chunks.extend(method_chunks)

            logger.debug(
                f"Created {len(chunks)} chunks from {parsed.filepath}: "
                f"1 file, {len(class_chunks)} classes, {len(method_chunks)} methods"
            )

        except Exception as e:
            logger.error(f"Failed to chunk {parsed.filepath}: {e}")

        return chunks

    def _create_file_chunk(self, parsed: ParsedFile, mtime: float) -> CodeChunk:
        """
        Create file-level overview chunk.

        Includes:
        - All imports
        - Top-level docstrings
        - Class and function names (structure overview)
        """
        # Build file overview
        lines = []

        # Imports
        if parsed.imports:
            lines.append("# Imports")
            lines.extend(parsed.imports)
            lines.append("")

        # Docstrings
        if parsed.docstrings:
            lines.append("# Documentation")
            lines.extend(parsed.docstrings[:2])  # First 2 docstrings
            lines.append("")

        # Structure overview
        lines.append("# Structure")
        if parsed.classes:
            lines.append(f"Classes: {', '.join(c.name for c in parsed.classes)}")
        if parsed.functions:
            lines.append(f"Functions: {', '.join(f.name for f in parsed.functions)}")

        content = '\n'.join(lines)

        # Truncate if too long
        if len(content) > self.CHUNK_SIZES['file']:
            content = content[:self.CHUNK_SIZES['file']] + '\n...'

        return CodeChunk(
            content=content,
            filepath=parsed.filepath,
            language=parsed.language,
            chunk_type=ChunkType.FILE,
            name=Path(parsed.filepath).name,
            dependencies=parsed.imports,
            line_range=(1, len(parsed.raw_content.split('\n'))),
            last_modified=mtime,
        )

    def _create_class_chunks(
        self,
        parsed: ParsedFile,
        parent_id: str,
        mtime: float
    ) -> List[CodeChunk]:
        """
        Create class-level chunks.

        Each chunk includes:
        - Class definition
        - Class docstring
        - Method signatures (names)
        - Attributes
        """
        chunks = []
        lines = parsed.raw_content.split('\n')

        for cls in parsed.classes:
            # Extract class content
            class_lines = lines[cls.start_line - 1:cls.end_line]
            content = '\n'.join(class_lines)

            # Build class overview (if content too long)
            if len(content) > self.CHUNK_SIZES['class']:
                overview_lines = []
                overview_lines.append(f"class {cls.name}:")
                if cls.docstring:
                    overview_lines.append(f'    """{cls.docstring}"""')
                if cls.methods:
                    overview_lines.append("\n    # Methods:")
                    for method in cls.methods:
                        overview_lines.append(f"    def {method.name}(...)")
                content = '\n'.join(overview_lines)

            chunk = CodeChunk(
                content=content,
                filepath=parsed.filepath,
                language=parsed.language,
                chunk_type=ChunkType.CLASS,
                parent_id=parent_id,
                name=cls.name,
                docstring=cls.docstring,
                dependencies=parsed.imports,
                line_range=(cls.start_line, cls.end_line),
                last_modified=mtime,
            )
            chunks.append(chunk)

        return chunks

    def _create_method_chunks(
        self,
        parsed: ParsedFile,
        parent_id: str,
        mtime: float
    ) -> List[CodeChunk]:
        """
        Create method/function-level chunks.

        Each chunk includes:
        - Complete function/method implementation
        - Signature
        - Docstring
        """
        chunks = []
        lines = parsed.raw_content.split('\n')

        # Standalone functions
        for func in parsed.functions:
            chunk = self._create_function_chunk(
                func, lines, parsed, parent_id, mtime, ChunkType.FUNCTION
            )
            if chunk:
                chunks.append(chunk)

        # Methods from classes
        for cls in parsed.classes:
            for method in cls.methods:
                chunk = self._create_function_chunk(
                    method, lines, parsed, parent_id, mtime, ChunkType.METHOD
                )
                if chunk:
                    chunks.append(chunk)

        return chunks

    def _create_function_chunk(
        self,
        func,
        lines: List[str],
        parsed: ParsedFile,
        parent_id: str,
        mtime: float,
        chunk_type: ChunkType
    ) -> CodeChunk:
        """Create chunk for a single function/method."""
        # Extract function content
        func_lines = lines[func.start_line - 1:func.end_line]
        content = '\n'.join(func_lines)

        # Truncate if too long (keep signature + docstring)
        if len(content) > self.CHUNK_SIZES['method']:
            truncated_lines = []
            # Keep first 10 lines (signature + docstring usually)
            truncated_lines.extend(func_lines[:10])
            truncated_lines.append("    # ... implementation truncated ...")
            # Keep last 3 lines (often return statement)
            truncated_lines.extend(func_lines[-3:])
            content = '\n'.join(truncated_lines)

        return CodeChunk(
            content=content,
            filepath=parsed.filepath,
            language=parsed.language,
            chunk_type=chunk_type,
            parent_id=parent_id,
            name=func.name,
            signature=func.signature,
            docstring=func.docstring,
            dependencies=parsed.imports,
            line_range=(func.start_line, func.end_line),
            last_modified=mtime,
        )

    async def chunk_files(self, parsed_files: List[ParsedFile]) -> List[CodeChunk]:
        """
        Chunk multiple files.

        Args:
            parsed_files: List of parsed files

        Returns:
            Flat list of all chunks
        """
        all_chunks = []

        for parsed in parsed_files:
            chunks = await self.chunk_file(parsed)
            all_chunks.extend(chunks)

        logger.info(f"Created {len(all_chunks)} total chunks from {len(parsed_files)} files")
        return all_chunks
