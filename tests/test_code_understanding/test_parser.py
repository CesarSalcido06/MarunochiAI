"""Tests for CodeParser."""

import pytest
from pathlib import Path
import tempfile

from marunochithe.code_understanding.parser import CodeParser
from marunochithe.code_understanding.models import Language


@pytest.fixture
def parser():
    """Create CodeParser instance."""
    return CodeParser()


@pytest.fixture
def temp_python_file():
    """Create temporary Python file for testing."""
    content = '''"""Module docstring."""

import os
from typing import List

def hello_world(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

class Calculator:
    """A simple calculator class."""

    def add(self, a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    def multiply(self, a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b
'''
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(content)
        filepath = f.name

    yield filepath

    # Cleanup
    Path(filepath).unlink()


@pytest.mark.asyncio
async def test_parse_python_function(parser, temp_python_file):
    """Test parsing a Python function."""
    result = await parser.parse_file(temp_python_file)

    assert result is not None
    assert result.language == Language.PYTHON
    assert len(result.functions) >= 1

    # Check hello_world function
    hello_func = next((f for f in result.functions if f.name == 'hello_world'), None)
    assert hello_func is not None
    assert hello_func.docstring is not None
    assert 'Greet someone' in hello_func.docstring


@pytest.mark.asyncio
async def test_parse_python_class(parser, temp_python_file):
    """Test parsing a Python class."""
    result = await parser.parse_file(temp_python_file)

    assert result is not None
    assert len(result.classes) >= 1

    # Check Calculator class
    calc_class = next((c for c in result.classes if c.name == 'Calculator'), None)
    assert calc_class is not None
    assert calc_class.docstring is not None
    assert 'calculator' in calc_class.docstring.lower()
    assert len(calc_class.methods) >= 2


@pytest.mark.asyncio
async def test_parse_imports(parser, temp_python_file):
    """Test extracting imports."""
    result = await parser.parse_file(temp_python_file)

    assert result is not None
    assert len(result.imports) >= 1
    assert any('import os' in imp for imp in result.imports)


@pytest.mark.asyncio
async def test_parse_file_cached(parser, temp_python_file):
    """Test caching mechanism."""
    # First parse (fresh)
    result1 = await parser.parse_file_cached(temp_python_file)
    assert result1 is not None

    # Second parse (should use cache)
    result2 = await parser.parse_file_cached(temp_python_file)
    assert result2 is not None
    assert result1.filepath == result2.filepath

    # Verify cache was used
    assert temp_python_file in parser.cache


@pytest.mark.asyncio
async def test_parse_nonexistent_file(parser):
    """Test parsing a file that doesn't exist."""
    result = await parser.parse_file('/nonexistent/file.py')
    assert result is None


@pytest.mark.asyncio
async def test_language_detection(parser):
    """Test language detection from file extension."""
    assert parser._detect_language(Path('test.py')) == Language.PYTHON
    assert parser._detect_language(Path('test.js')) == Language.JAVASCRIPT
    assert parser._detect_language(Path('test.ts')) == Language.TYPESCRIPT
    assert parser._detect_language(Path('test.txt')) == Language.UNKNOWN


@pytest.mark.asyncio
async def test_clear_cache(parser, temp_python_file):
    """Test cache clearing."""
    # Parse and cache
    await parser.parse_file_cached(temp_python_file)
    assert len(parser.cache) > 0

    # Clear cache
    parser.clear_cache()
    assert len(parser.cache) == 0
