"""Command-line interface for MarunochiAI."""

import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from loguru import logger

from ..config import load_settings
from ..core.inference import InferenceEngine
from ..core.tools import ToolRegistry
from ..code_understanding import (
    CodeParser,
    CodeChunker,
    CodebaseIndexer,
    KeywordIndexer,
    HybridSearcher,
    CodebaseWatcher,
)

app = typer.Typer(
    name="marunochithe",
    help="MarunochiAI - The most powerful self-hosted coding assistant",
    add_completion=False,
)

console = Console()


@app.command()
def chat(
    prompt: str = typer.Argument(..., help="Your coding question or request"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Model to use (7b, 14b, custom)"),
    stream: bool = typer.Option(True, "--stream/--no-stream", help="Stream response"),
):
    """
    Chat with MarunochiAI.

    Examples:
        marunochithe chat "Write a Python function to reverse a string"
        marunochithe chat "Refactor main.py to use async/await" --model 14b
    """
    asyncio.run(_chat(prompt, model, stream))


async def _chat(prompt: str, model: Optional[str], stream: bool):
    """Internal async chat handler."""
    try:
        # Load configuration and initialize engine
        settings = load_settings()
        engine = InferenceEngine(
            ollama_host=settings.ollama.host,
            enable_custom=settings.server.enable_custom
        )

        # Prepare messages
        messages = [{"role": "user", "content": prompt}]

        console.print(f"\n[bold blue]You:[/bold blue] {prompt}\n")

        if stream:
            console.print("[bold green]MarunochiAI:[/bold green] ", end="")

            async for token in await engine.chat(messages, stream=True):
                console.print(token, end="")

            console.print("\n")  # New line after streaming
        else:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("Thinking...", total=None)

                response = await engine.chat(messages, stream=False)

                progress.update(task, completed=True)

            console.print(f"\n[bold green]MarunochiAI:[/bold green]\n")
            console.print(Markdown(response))

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def read(
    filepath: str = typer.Argument(..., help="File to read"),
):
    """
    Read a file and display its contents.

    Example:
        marunochithe read main.py
    """
    asyncio.run(_read(filepath))


async def _read(filepath: str):
    """Internal async read handler."""
    try:
        result = await ToolRegistry.read_file(filepath)

        if "error" in result:
            console.print(f"[bold red]Error:[/bold red] {result['error']}")
            raise typer.Exit(code=1)

        console.print(f"\n[bold blue]File:[/bold blue] {result['filepath']}")
        console.print(f"[dim]Lines: {result['lines']} | Size: {result['size']} bytes[/dim]\n")
        console.print(result["content"])

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def write(
    filepath: str = typer.Argument(..., help="File to write"),
    content: str = typer.Argument(..., help="Content to write"),
):
    """
    Write content to a file.

    Example:
        marunochithe write test.py "print('Hello, World!')"
    """
    asyncio.run(_write(filepath, content))


async def _write(filepath: str, content: str):
    """Internal async write handler."""
    try:
        result = await ToolRegistry.write_file(filepath, content)

        if result["status"] == "success":
            console.print(f"[bold green]✓[/bold green] Written {result['bytes_written']} bytes to {result['filepath']}")
        else:
            console.print(f"[bold red]Error:[/bold red] {result.get('error', 'Unknown error')}")
            raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def git_status(
    repo_path: str = typer.Option(".", "--path", "-p", help="Repository path"),
):
    """
    Show git repository status.

    Example:
        marunochithe git-status
        marunochithe git-status --path ~/MyProject
    """
    asyncio.run(_git_status(repo_path))


async def _git_status(repo_path: str):
    """Internal async git status handler."""
    try:
        result = await ToolRegistry.git_status(repo_path)

        if "error" in result:
            console.print(f"[bold red]Error:[/bold red] {result['error']}")
            raise typer.Exit(code=1)

        console.print(f"\n[bold blue]Branch:[/bold blue] {result['branch']}")
        console.print(f"[bold blue]HEAD:[/bold blue] {result['head_commit']}")
        console.print(f"[bold blue]Dirty:[/bold blue] {result['is_dirty']}\n")

        if result["staged"]:
            console.print("[bold green]Staged files:[/bold green]")
            for f in result["staged"]:
                console.print(f"  + {f}")

        if result["modified"]:
            console.print("[bold yellow]Modified files:[/bold yellow]")
            for f in result["modified"]:
                console.print(f"  M {f}")

        if result["untracked"]:
            console.print("[bold red]Untracked files:[/bold red]")
            for f in result["untracked"]:
                console.print(f"  ? {f}")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def server(
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(8765, "--port", "-p", help="Port to bind to"),
    reload: bool = typer.Option(False, "--reload", help="Enable auto-reload"),
):
    """
    Start the MarunochiAI API server.

    Example:
        marunochithe server
        marunochithe server --port 9000 --reload
    """
    import uvicorn
    from ..api.server import app as fastapi_app

    console.print(f"[bold green]Starting MarunochiAI server on {host}:{port}[/bold green]")

    uvicorn.run(
        "marunochithe.api.server:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info",
    )


@app.command()
def index(
    codebase_path: str = typer.Argument(".", help="Path to codebase"),
    watch: bool = typer.Option(False, "--watch", "-w", help="Watch for file changes"),
):
    """
    Index codebase for semantic search.

    Examples:
        marunochithe index
        marunochithe index ~/MyProject --watch
    """
    asyncio.run(_index(codebase_path, watch))


async def _index(codebase_path: str, watch: bool):
    """Internal async index handler."""
    try:
        console.print(f"\n[bold blue]Indexing codebase:[/bold blue] {codebase_path}")

        # Initialize components
        parser = CodeParser()
        chunker = CodeChunker()
        vector_indexer = CodebaseIndexer(collection_name="marunochithe_codebase")
        keyword_indexer = KeywordIndexer()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Parsing and indexing files...", total=None)

            # Index codebase
            result = await vector_indexer.index_codebase(codebase_path)

            # Also index in keyword DB
            all_chunks = []
            for filepath in Path(codebase_path).rglob("*.py"):
                parsed = await parser.parse_file(str(filepath))
                if parsed:
                    chunks = await chunker.chunk_file(parsed)
                    all_chunks.extend(chunks)

            if all_chunks:
                await keyword_indexer.index_chunks(all_chunks)

            progress.update(task, completed=True)

        # Display results
        console.print(f"\n[bold green]✓ Indexing complete![/bold green]")
        console.print(f"  Files indexed: {result['total_files']}")
        console.print(f"  Total chunks: {result['total_chunks']}")
        console.print(f"  Duration: {result['duration_ms']}ms")

        # Start watcher if requested
        if watch:
            console.print(f"\n[bold yellow]Watching for changes...[/bold yellow]")
            console.print("[dim]Press Ctrl+C to stop[/dim]\n")

            watcher = CodebaseWatcher(
                codebase_path=codebase_path,
                vector_indexer=vector_indexer,
                keyword_indexer=keyword_indexer,
                debounce_ms=500
            )

            await watcher.start_watching()

            # Keep running
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                console.print("\n[yellow]Stopped watching[/yellow]")
                watcher.stop_watching()

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        logger.exception("Indexing failed")
        raise typer.Exit(code=1)


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    limit: int = typer.Option(5, "--limit", "-l", help="Max results"),
    mode: str = typer.Option("hybrid", "--mode", "-m", help="Search mode (vector/keyword/hybrid)"),
    show_content: bool = typer.Option(True, "--content/--no-content", help="Show code content"),
):
    """
    Search codebase semantically.

    Examples:
        marunochithe search "authentication function"
        marunochithe search "database query" --limit 10
        marunochithe search "user management" --mode vector
    """
    asyncio.run(_search(query, limit, mode, show_content))


async def _search(query: str, limit: int, mode: str, show_content: bool):
    """Internal async search handler."""
    try:
        console.print(f"\n[bold blue]Searching for:[/bold blue] {query}")
        console.print(f"[dim]Mode: {mode} | Limit: {limit}[/dim]\n")

        # Initialize searcher
        vector_indexer = CodebaseIndexer(collection_name="marunochithe_codebase")
        keyword_indexer = KeywordIndexer()
        searcher = HybridSearcher(
            vector_indexer=vector_indexer,
            keyword_indexer=keyword_indexer,
            rrf_k=60
        )

        # Search
        results = await searcher.search(query, mode=mode, limit=limit)

        if not results:
            console.print("[yellow]No results found[/yellow]")
            return

        # Display results
        console.print(f"[bold green]Found {len(results)} results:[/bold green]\n")

        for i, result in enumerate(results, 1):
            console.print(f"[bold]{i}. {result.name}[/bold]")
            console.print(f"   [dim]{result.filepath}:{result.line_range[0]}[/dim]")
            console.print(f"   [cyan]Similarity: {result.similarity:.3f}[/cyan]")
            console.print(f"   [dim]Language: {result.language.value} | Type: {result.chunk_type}[/dim]")

            if show_content:
                # Show code snippet with syntax highlighting
                from rich.syntax import Syntax

                # Limit content to first 10 lines for display
                content_lines = result.content.split('\n')[:10]
                content_preview = '\n'.join(content_lines)
                if len(result.content.split('\n')) > 10:
                    content_preview += '\n...'

                syntax = Syntax(
                    content_preview,
                    result.language.value,
                    theme="monokai",
                    line_numbers=True,
                    start_line=result.line_range[0]
                )
                console.print(syntax)

            console.print()  # Blank line between results

        await keyword_indexer.close()

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        logger.exception("Search failed")
        raise typer.Exit(code=1)


@app.command()
def version():
    """Show MarunochiAI version."""
    from .. import __version__

    console.print(f"[bold blue]MarunochiAI[/bold blue] version [bold green]{__version__}[/bold green]")
    console.print("The most powerful self-hosted coding assistant")


if __name__ == "__main__":
    app()
