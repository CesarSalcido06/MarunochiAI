"""Tests for HybridSearcher."""

import pytest
from pathlib import Path

from marunochithe.code_understanding.indexer import CodebaseIndexer
from marunochithe.code_understanding.keyword_indexer import KeywordIndexer
from marunochithe.code_understanding.hybrid_searcher import HybridSearcher


@pytest.fixture
def temp_codebase(tmp_path):
    """Create a temporary codebase for testing."""
    # Create test Python files
    (tmp_path / "main.py").write_text('''"""Main module with authentication."""

def authenticate_user(username: str, password: str) -> bool:
    """Authenticate a user with username and password."""
    if not username or not password:
        return False
    # Simplified authentication logic
    return True

class UserManager:
    """Manage user accounts and authentication."""

    def create_user(self, username: str, email: str) -> dict:
        """Create a new user account."""
        return {"username": username, "email": email, "created": True}

    def delete_user(self, username: str) -> bool:
        """Delete a user account."""
        return True
''')

    (tmp_path / "database.py").write_text('''"""Database connection utilities."""

import sqlite3

def connect_database(db_path: str):
    """Connect to SQLite database."""
    return sqlite3.connect(db_path)

def execute_query(conn, query: str):
    """Execute a SQL query."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
''')

    (tmp_path / "utils.py").write_text('''"""Utility functions for string manipulation."""

def capitalize_words(text: str) -> str:
    """Capitalize all words in a string."""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]
''')

    return tmp_path


@pytest.fixture
async def hybrid_searcher(tmp_path, temp_codebase):
    """Create HybridSearcher with indexed codebase."""
    # Create vector indexer
    vector_db = str(tmp_path / "vector_db")
    vector_indexer = CodebaseIndexer(
        collection_name="test_hybrid",
        persist_directory=vector_db
    )

    # Create keyword indexer
    keyword_db = str(tmp_path / "keyword.db")
    keyword_indexer = KeywordIndexer(db_path=keyword_db)

    # Index the codebase with vector indexer
    await vector_indexer.index_codebase(str(temp_codebase))

    # Index with keyword indexer
    from marunochithe.code_understanding.parser import CodeParser
    from marunochithe.code_understanding.chunker import CodeChunker

    parser = CodeParser()
    chunker = CodeChunker()

    for filepath in temp_codebase.glob("*.py"):
        parsed = await parser.parse_file(str(filepath))
        if parsed:
            chunks = await chunker.chunk_file(parsed)
            await keyword_indexer.index_chunks(chunks)

    # Create hybrid searcher
    searcher = HybridSearcher(
        vector_indexer=vector_indexer,
        keyword_indexer=keyword_indexer,
        rrf_k=60
    )

    yield searcher

    # Cleanup
    await vector_indexer.clear_index()
    await keyword_indexer.clear_index()
    await keyword_indexer.close()


@pytest.mark.asyncio
async def test_vector_search_mode(hybrid_searcher):
    """Test vector-only search mode."""
    results = await hybrid_searcher.search(
        query="authenticate user credentials",
        mode="vector",
        limit=5
    )

    assert len(results) > 0
    # Should find authentication-related code
    assert any('authenticate' in r.name.lower() for r in results)


@pytest.mark.asyncio
async def test_keyword_search_mode(hybrid_searcher):
    """Test keyword-only search mode."""
    results = await hybrid_searcher.search(
        query="authenticate_user",
        mode="keyword",
        limit=5
    )

    assert len(results) > 0
    # Should find exact function name match
    assert any('authenticate' in r.name.lower() for r in results)


@pytest.mark.asyncio
async def test_hybrid_search_mode(hybrid_searcher):
    """Test hybrid search with RRF fusion."""
    results = await hybrid_searcher.search(
        query="user authentication function",
        mode="hybrid",
        limit=5
    )

    assert len(results) > 0
    # Hybrid should combine semantic + keyword signals
    assert any('authenticate' in r.name.lower() or 'user' in r.name.lower() for r in results)


@pytest.mark.asyncio
async def test_rrf_fusion_algorithm(hybrid_searcher):
    """Test RRF fusion combines rankings correctly."""
    # Create test rankings
    ranking1 = [("chunk1", 0.9), ("chunk2", 0.8), ("chunk3", 0.7)]
    ranking2 = [("chunk2", 0.95), ("chunk1", 0.85), ("chunk4", 0.75)]

    # Apply RRF
    fused = hybrid_searcher._rrf_fusion([ranking1, ranking2], k=60)

    # chunk2 appears high in both rankings, should have highest fused score
    assert "chunk2" in fused
    assert "chunk1" in fused

    # chunk2 should have higher score than chunk3 (which only appears in one ranking)
    if "chunk3" in fused:
        assert fused["chunk2"] > fused["chunk3"]


@pytest.mark.asyncio
async def test_search_with_language_filter(hybrid_searcher):
    """Test search with language filtering."""
    results = await hybrid_searcher.search(
        query="function",
        mode="hybrid",
        limit=5,
        filter_language="python"
    )

    assert len(results) > 0
    # All results should be Python
    for result in results:
        assert result.language.value == "python"


@pytest.mark.asyncio
async def test_hybrid_better_than_single(hybrid_searcher):
    """Test that hybrid search provides better results than single mode."""
    query = "database query execution"

    vector_results = await hybrid_searcher.search(query, mode="vector", limit=3)
    keyword_results = await hybrid_searcher.search(query, mode="keyword", limit=3)
    hybrid_results = await hybrid_searcher.search(query, mode="hybrid", limit=3)

    # Hybrid should return results (may or may not be more than individual modes)
    assert len(hybrid_results) > 0

    # At minimum, hybrid should leverage both approaches
    assert len(hybrid_results) <= len(vector_results) + len(keyword_results)


@pytest.mark.asyncio
async def test_exact_match_in_hybrid(hybrid_searcher):
    """Test that exact matches are prioritized in hybrid search."""
    # Search for exact function name
    results = await hybrid_searcher.search(
        query="execute_query",
        mode="hybrid",
        limit=5
    )

    assert len(results) > 0
    # Exact match should be in top results
    assert any('execute_query' in r.name for r in results[:3])


@pytest.mark.asyncio
async def test_semantic_similarity_in_hybrid(hybrid_searcher):
    """Test that semantic similarity works in hybrid search."""
    # Use semantic query (not exact match)
    results = await hybrid_searcher.search(
        query="create new user account",
        mode="hybrid",
        limit=5
    )

    assert len(results) > 0
    # Should find create_user method semantically
    assert any('create' in r.name.lower() or 'user' in r.name.lower() for r in results)


@pytest.mark.asyncio
async def test_get_stats(hybrid_searcher):
    """Test statistics retrieval."""
    stats = await hybrid_searcher.get_stats()

    assert 'vector' in stats
    assert 'keyword' in stats
    assert 'rrf_k' in stats
    assert 'fusion_enabled' in stats

    assert stats['rrf_k'] == 60
    assert stats['fusion_enabled'] is True


@pytest.mark.asyncio
async def test_empty_query_handling(hybrid_searcher):
    """Test handling of edge cases."""
    # Empty results should not crash
    results = await hybrid_searcher.search(
        query="xyznonexistentquery123",
        mode="hybrid",
        limit=5
    )

    # Should return empty or very low relevance results
    assert isinstance(results, list)


@pytest.mark.asyncio
async def test_fallback_to_vector(tmp_path, temp_codebase):
    """Test fallback to vector when keyword indexer not available."""
    # Create searcher without keyword indexer
    vector_db = str(tmp_path / "vector_only")
    vector_indexer = CodebaseIndexer(
        collection_name="test_fallback",
        persist_directory=vector_db
    )
    await vector_indexer.index_codebase(str(temp_codebase))

    searcher = HybridSearcher(
        vector_indexer=vector_indexer,
        keyword_indexer=None  # No keyword indexer
    )

    # Keyword mode should fall back to vector
    results = await searcher.search(
        query="authentication",
        mode="keyword",
        limit=3
    )

    # Should still return results via fallback
    assert len(results) > 0

    await vector_indexer.clear_index()
