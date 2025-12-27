"""Command-line interface for MarunochiAI."""

import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from loguru import logger

from ..core.inference import InferenceEngine
from ..core.tools import ToolRegistry

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
        # Initialize engine
        engine = InferenceEngine()

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
def version():
    """Show MarunochiAI version."""
    from .. import __version__

    console.print(f"[bold blue]MarunochiAI[/bold blue] version [bold green]{__version__}[/bold green]")
    console.print("The most powerful self-hosted coding assistant")


if __name__ == "__main__":
    app()
