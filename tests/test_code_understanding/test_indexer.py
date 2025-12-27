"""Tests for CodebaseIndexer."""

import pytest
import tempfile
import shutil
from pathlib import Path

from marunochithe.code_understanding.indexer import CodebaseIndexer


@pytest.fixture
def temp_codebase(tmp_path):
    """Create a temporary codebase for testing."""
    # Create test Python files
    (tmp_path / "main.py").write_text('''"""Main module."""

def hello(name: str) -> str:
    """Say hello."""
    return f"Hello, {name}!"

class Greeter:
    """A greeter class."""

    def greet(self, name: str) -> str:
        """Greet someone."""
        return f"Greetings, {name}!"
''')

    (tmp_path / "utils.py").write_text('''"""Utility functions."""

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
''')

    # Create a subdirectory with code
    subdir = tmp_path / "lib"
    subdir.mkdir()

    (subdir / "helper.py").write_text('''"""Helper module."""

class Helper:
    """A helper class."""

    def help(self) -> str:
        """Provide help."""
        return "Here to help!"
''')

    return tmp_path


@pytest.fixture
async def indexer(tmp_path):
    """Create CodebaseIndexer with temporary database."""
    # Use a temporary directory for ChromaDB
    db_path = str(tmp_path / "test_chroma")

    indexer = CodebaseIndexer(
        collection_name="test_collection",
        persist_directory=db_path
    )

    yield indexer

    # Cleanup
    try:
        await indexer.clear_index()
    except:
        pass


@pytest.mark.asyncio
async def test_index_codebase(indexer, temp_codebase):
    """Test indexing an entire codebase."""
    result = await indexer.index_codebase(str(temp_codebase))

    assert result['total_files'] == 3
    assert result['successful_files'] == 3
    assert result['total_chunks'] > 0
    assert result['indexed_chunks'] > 0
    assert result['duration_ms'] > 0


@pytest.mark.asyncio
async def test_search_functionality(indexer, temp_codebase):
    """Test semantic search."""
    # Index the codebase
    await indexer.index_codebase(str(temp_codebase))

    # Search for "add two numbers"
    results = await indexer.search("add two numbers", limit=5)

    assert len(results) > 0
    # Should find the add function
    assert any('add' in r.name.lower() for r in results)


@pytest.mark.asyncio
async def test_search_with_filter(indexer, temp_codebase):
    """Test search with metadata filters."""
    # Index the codebase
    await indexer.index_codebase(str(temp_codebase))

    # Search only in Python files (should work for all)
    results = await indexer.search(
        "function",
        limit=5,
        filter_metadata={"language": "python"}
    )

    assert len(results) > 0
    # All results should be Python
    for result in results:
        assert result.language.value == "python"


@pytest.mark.asyncio
async def test_index_single_file(indexer, tmp_path):
    """Test indexing a single file."""
    # Create a test file
    test_file = tmp_path / "test.py"
    test_file.write_text('''def test_func():
    """Test function."""
    return 42
''')

    # Index the file
    result = await indexer.index_file(str(test_file))

    assert result['filepath'] == str(test_file)
    assert result['chunks_added'] > 0
    assert result['duration_ms'] >= 0


@pytest.mark.asyncio
async def test_delete_file(indexer, temp_codebase):
    """Test deleting a file from the index."""
    # Index the codebase
    await indexer.index_codebase(str(temp_codebase))

    # Get initial stats
    stats_before = await indexer.get_stats()
    total_before = stats_before['total_chunks']

    # Delete one file
    test_file = str(temp_codebase / "main.py")
    await indexer.delete_file(test_file)

    # Get stats after deletion
    stats_after = await indexer.get_stats()
    total_after = stats_after['total_chunks']

    # Should have fewer chunks
    assert total_after < total_before


@pytest.mark.asyncio
async def test_get_stats(indexer, temp_codebase):
    """Test getting indexing statistics."""
    # Index the codebase
    await indexer.index_codebase(str(temp_codebase))

    # Get stats
    stats = await indexer.get_stats()

    assert stats['total_chunks'] > 0
    assert stats['total_files'] == 3
    assert 'python' in stats['languages']
    assert stats['languages']['python'] > 0

    # Should have different chunk types
    assert 'file' in stats['chunk_types']


@pytest.mark.asyncio
async def test_incremental_update(indexer, temp_codebase):
    """Test incremental file update."""
    # Initial index
    await indexer.index_codebase(str(temp_codebase))

    # Modify a file
    test_file = temp_codebase / "utils.py"
    test_file.write_text('''"""Updated utils."""

def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b
''')

    # Re-index the modified file
    result = await indexer.index_file(str(test_file))

    assert result['chunks_added'] > 0

    # Search for new content
    results = await indexer.search("subtract", limit=5)
    assert len(results) > 0
    assert any('subtract' in r.name.lower() for r in results)


@pytest.mark.asyncio
async def test_clear_index(indexer, temp_codebase):
    """Test clearing the entire index."""
    # Index the codebase
    await indexer.index_codebase(str(temp_codebase))

    # Verify data exists
    stats_before = await indexer.get_stats()
    assert stats_before['total_chunks'] > 0

    # Clear index
    await indexer.clear_index()

    # Verify data is gone
    stats_after = await indexer.get_stats()
    assert stats_after['total_chunks'] == 0


@pytest.mark.asyncio
async def test_empty_codebase(indexer, tmp_path):
    """Test indexing an empty directory."""
    # Create empty directory
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()

    # Index it
    result = await indexer.index_codebase(str(empty_dir))

    assert result['total_files'] == 0
    assert result['total_chunks'] == 0


@pytest.mark.asyncio
async def test_search_no_results(indexer, temp_codebase):
    """Test search with no matching results."""
    # Index the codebase
    await indexer.index_codebase(str(temp_codebase))

    # Search for something that doesn't exist
    results = await indexer.search("xyzabc123nonexistent")

    # Should return results (even if not perfect matches)
    # or empty list if no results
    assert isinstance(results, list)
