#!/usr/bin/env python3
"""
Quick validation test for Phase 2: Code Understanding

Tests all Phase 2 components to verify functionality.
"""

import asyncio
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

async def test_imports():
    """Test if all Phase 2 modules can be imported."""
    console.print("\n[bold cyan]Testing Phase 2 Imports...[/bold cyan]")

    results = []

    try:
        from marunochithe.code_understanding import CodeParser
        results.append(("CodeParser", "✅ OK", "Tree-sitter AST parsing"))
    except Exception as e:
        results.append(("CodeParser", f"❌ FAIL", str(e)[:50]))

    try:
        from marunochithe.code_understanding import CodeChunker
        results.append(("CodeChunker", "✅ OK", "Hierarchical chunking"))
    except Exception as e:
        results.append(("CodeChunker", f"❌ FAIL", str(e)[:50]))

    try:
        from marunochithe.code_understanding import CodebaseIndexer
        results.append(("CodebaseIndexer", "✅ OK", "ChromaDB indexing"))
    except Exception as e:
        results.append(("CodebaseIndexer", f"❌ FAIL", str(e)[:50]))

    try:
        from marunochithe.code_understanding import HybridSearcher
        results.append(("HybridSearcher", "✅ OK", "Hybrid search (Vector+BM25+RRF)"))
    except Exception as e:
        results.append(("HybridSearcher", f"❌ FAIL", str(e)[:50]))

    try:
        from marunochithe.code_understanding import CodebaseWatcher
        results.append(("CodebaseWatcher", "✅ OK", "Incremental file watching"))
    except Exception as e:
        results.append(("CodebaseWatcher", f"❌ FAIL", str(e)[:50]))

    # Display results
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Component", style="white")
    table.add_column("Status", justify="center")
    table.add_column("Description", style="dim")

    for component, status, desc in results:
        table.add_row(component, status, desc)

    console.print(table)

    passed = sum(1 for _, status, _ in results if "✅" in status)
    total = len(results)

    return passed, total


async def test_parser():
    """Test CodeParser functionality."""
    console.print("\n[bold cyan]Testing CodeParser...[/bold cyan]")

    try:
        from marunochithe.code_understanding import CodeParser

        parser = CodeParser()

        # Create test file
        test_file = Path("/tmp/test_parse.py")
        test_file.write_text('''
def hello_world(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"

class Calculator:
    """Simple calculator."""
    def add(self, a: int, b: int) -> int:
        return a + b
''')

        # Parse it
        result = await parser.parse_file(str(test_file))

        if result:
            console.print(f"  ✅ Parsed {test_file.name}")
            console.print(f"  Functions found: {len(result.functions)}")
            console.print(f"  Classes found: {len(result.classes)}")
            return True
        else:
            console.print("  ❌ Parse returned None")
            return False

    except Exception as e:
        console.print(f"  ❌ Parser test failed: {e}")
        return False


async def test_chunker():
    """Test CodeChunker functionality."""
    console.print("\n[bold cyan]Testing CodeChunker...[/bold cyan]")

    try:
        from marunochithe.code_understanding import CodeParser, CodeChunker

        parser = CodeParser()
        chunker = CodeChunker()

        # Create test file
        test_file = Path("/tmp/test_chunk.py")
        test_file.write_text('''
def greet(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"
''')

        # Parse then chunk
        parsed = await parser.parse_file(str(test_file))
        if parsed:
            chunks = await chunker.chunk_file(parsed)
            console.print(f"  ✅ Generated {len(chunks)} chunks")
            return len(chunks) > 0
        else:
            console.print("  ❌ Parsing failed")
            return False

    except Exception as e:
        console.print(f"  ❌ Chunker test failed: {e}")
        return False


async def main():
    """Run all validation tests."""
    console.print(Panel.fit(
        "[bold magenta]Phase 2: Code Understanding - Validation[/bold magenta]\n"
        "Testing all components...",
        border_style="magenta"
    ))

    # Test imports
    passed_imports, total_imports = await test_imports()

    # Test functionality
    tests = [
        test_parser(),
        test_chunker(),
    ]

    results = await asyncio.gather(*tests, return_exceptions=True)
    passed_func = sum(1 for r in results if r is True)
    total_func = len(tests)

    # Summary
    console.print(f"\n[bold]Validation Summary:[/bold]")
    console.print(f"  Imports: {passed_imports}/{total_imports} ✅")
    console.print(f"  Functional Tests: {passed_func}/{total_func} ✅")

    total_passed = passed_imports + passed_func
    total_tests = total_imports + total_func

    if total_passed == total_tests:
        console.print(f"\n[bold green]✅ Phase 2 validation PASSED ({total_passed}/{total_tests})[/bold green]")
        return 0
    else:
        console.print(f"\n[bold yellow]⚠️  Phase 2 validation PARTIAL ({total_passed}/{total_tests})[/bold yellow]")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
