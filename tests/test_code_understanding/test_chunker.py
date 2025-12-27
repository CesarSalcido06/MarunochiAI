"""Tests for CodeChunker."""

import pytest
from pathlib import Path

from marunochithe.code_understanding.chunker import CodeChunker
from marunochithe.code_understanding.parser import CodeParser
from marunochithe.code_understanding.models import ChunkType, Language


@pytest.fixture
def chunker():
    """Create CodeChunker instance."""
    return CodeChunker()


@pytest.fixture
def parser():
    """Create CodeParser instance."""
    return CodeParser()


@pytest.fixture
async def parsed_python_file(parser, tmp_path):
    """Create and parse a temporary Python file."""
    content = '''"""Test module."""

import os
from typing import List

def greet(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"

class Person:
    """A person class."""

    def __init__(self, name: str):
        """Initialize person."""
        self.name = name

    def say_hello(self) -> str:
        """Say hello."""
        return f"Hello, I'm {self.name}"
'''
    filepath = tmp_path / "test.py"
    filepath.write_text(content)

    parsed = await parser.parse_file(str(filepath))
    return parsed


@pytest.mark.asyncio
async def test_chunk_file(chunker, parsed_python_file):
    """Test chunking a parsed file."""
    chunks = await chunker.chunk_file(parsed_python_file)

    # Should have at least: 1 file chunk + classes/methods
    assert len(chunks) >= 1

    # Check file-level chunk
    file_chunks = [c for c in chunks if c.chunk_type == ChunkType.FILE]
    assert len(file_chunks) == 1
    assert 'import os' in file_chunks[0].content or 'Imports' in file_chunks[0].content


@pytest.mark.asyncio
async def test_hierarchical_chunking(chunker, parsed_python_file):
    """Test hierarchical structure (file -> class -> method)."""
    chunks = await chunker.chunk_file(parsed_python_file)

    # Get chunk types
    file_chunks = [c for c in chunks if c.chunk_type == ChunkType.FILE]
    class_chunks = [c for c in chunks if c.chunk_type == ChunkType.CLASS]
    method_chunks = [c for c in chunks if c.chunk_type == ChunkType.METHOD]
    function_chunks = [c for c in chunks if c.chunk_type == ChunkType.FUNCTION]

    # Should have all three levels
    assert len(file_chunks) == 1
    assert len(class_chunks) >= 1  # Person class
    assert (len(method_chunks) + len(function_chunks)) >= 1  # greet function + methods


@pytest.mark.asyncio
async def test_class_chunk_content(chunker, parsed_python_file):
    """Test class chunk contains expected content."""
    chunks = await chunker.chunk_file(parsed_python_file)

    class_chunks = [c for c in chunks if c.chunk_type == ChunkType.CLASS]
    assert len(class_chunks) >= 1

    person_chunk = next((c for c in class_chunks if c.name == 'Person'), None)
    assert person_chunk is not None
    assert 'Person' in person_chunk.content
    assert person_chunk.docstring is not None


@pytest.mark.asyncio
async def test_method_chunk_content(chunker, parsed_python_file):
    """Test method chunk contains expected content."""
    chunks = await chunker.chunk_file(parsed_python_file)

    method_chunks = [c for c in chunks if c.chunk_type == ChunkType.METHOD]
    function_chunks = [c for c in chunks if c.chunk_type == ChunkType.FUNCTION]

    # Should have greet function and Person methods
    assert len(method_chunks) + len(function_chunks) >= 2


@pytest.mark.asyncio
async def test_chunk_metadata(chunker, parsed_python_file):
    """Test chunk metadata is properly set."""
    chunks = await chunker.chunk_file(parsed_python_file)

    for chunk in chunks:
        assert chunk.id is not None
        assert chunk.filepath == parsed_python_file.filepath
        assert chunk.language == Language.PYTHON
        assert chunk.line_range[0] > 0
        assert chunk.line_range[1] >= chunk.line_range[0]
        assert chunk.last_modified > 0


@pytest.mark.asyncio
async def test_chunk_parent_relationships(chunker, parsed_python_file):
    """Test parent-child relationships in chunks."""
    chunks = await chunker.chunk_file(parsed_python_file)

    file_chunk = next(c for c in chunks if c.chunk_type == ChunkType.FILE)

    # Class and method chunks should have parent_id set to file chunk
    for chunk in chunks:
        if chunk.chunk_type in [ChunkType.CLASS, ChunkType.METHOD, ChunkType.FUNCTION]:
            assert chunk.parent_id == file_chunk.id


@pytest.mark.asyncio
async def test_chunk_size_limits(chunker, parsed_python_file):
    """Test chunks respect size limits."""
    chunks = await chunker.chunk_file(parsed_python_file)

    for chunk in chunks:
        if chunk.chunk_type == ChunkType.FILE:
            assert len(chunk.content) <= chunker.CHUNK_SIZES['file'] + 100  # Small tolerance
        elif chunk.chunk_type == ChunkType.CLASS:
            assert len(chunk.content) <= chunker.CHUNK_SIZES['class'] + 100
        elif chunk.chunk_type in [ChunkType.METHOD, ChunkType.FUNCTION]:
            assert len(chunk.content) <= chunker.CHUNK_SIZES['method'] + 100


@pytest.mark.asyncio
async def test_chunk_to_dict(chunker, parsed_python_file):
    """Test CodeChunk to_dict conversion."""
    chunks = await chunker.chunk_file(parsed_python_file)

    for chunk in chunks:
        chunk_dict = chunk.to_dict()

        assert 'id' in chunk_dict
        assert 'content' in chunk_dict
        assert 'filepath' in chunk_dict
        assert 'language' in chunk_dict
        assert 'chunk_type' in chunk_dict
        assert 'line_range' in chunk_dict
