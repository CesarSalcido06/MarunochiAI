#!/usr/bin/env python3
"""
Test script for A2A integration endpoints.

This script tests the agent card, sync, and task endpoints
to verify BenchAI integration is working correctly.
"""

import asyncio
import aiohttp
import json
from rich.console import Console
from rich.table import Table

console = Console()

MARUNOCHI_URL = "http://localhost:8765"


async def test_agent_card():
    """Test the agent card endpoint."""
    console.print("\n[bold blue]Testing Agent Card Endpoint[/bold blue]")
    console.print(f"GET {MARUNOCHI_URL}/.well-known/agent.json\n")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{MARUNOCHI_URL}/.well-known/agent.json") as response:
                if response.status == 200:
                    data = await response.json()
                    console.print("[green]✓[/green] Agent card retrieved successfully")
                    console.print(f"\n[cyan]Agent:[/cyan] {data['name']} v{data['version']}")
                    console.print(f"[cyan]Description:[/cyan] {data['description']}")
                    console.print(f"[cyan]Capabilities:[/cyan] {', '.join(data['capabilities'][:5])}...")
                    console.print(f"[cyan]Domains:[/cyan] {', '.join(data['domains'])}")
                    console.print(f"[cyan]Priority:[/cyan] {data['priority']}")
                    return True
                else:
                    console.print(f"[red]✗[/red] Failed with status {response.status}")
                    return False
    except Exception as e:
        console.print(f"[red]✗[/red] Error: {e}")
        return False


async def test_sync_receive():
    """Test the sync receive endpoint."""
    console.print("\n[bold blue]Testing Sync Receive Endpoint[/bold blue]")
    console.print(f"POST {MARUNOCHI_URL}/v1/sync/receive\n")

    payload = {
        "from_agent": "testAgent",
        "sync_type": "experience",
        "items": [
            {
                "id": "test-001",
                "content": "Test experience item",
                "importance": 5
            },
            {
                "id": "test-002",
                "content": "Another test experience",
                "importance": 4
            }
        ],
        "timestamp": "2025-12-27T00:00:00Z"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{MARUNOCHI_URL}/v1/sync/receive",
                json=payload
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    console.print("[green]✓[/green] Sync data received successfully")
                    console.print(f"[cyan]Items processed:[/cyan] {data['items_processed']}")
                    console.print(f"[cyan]From agent:[/cyan] {data['from_agent']}")
                    console.print(f"[cyan]Sync type:[/cyan] {data['sync_type']}")
                    return True
                else:
                    console.print(f"[red]✗[/red] Failed with status {response.status}")
                    return False
    except Exception as e:
        console.print(f"[red]✗[/red] Error: {e}")
        return False


async def test_sync_share():
    """Test the sync share endpoint."""
    console.print("\n[bold blue]Testing Sync Share Endpoint[/bold blue]")
    console.print(f"GET {MARUNOCHI_URL}/v1/sync/share\n")

    params = {
        "requester": "testAgent",
        "sync_type": "experience",
        "limit": 10
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{MARUNOCHI_URL}/v1/sync/share",
                params=params
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    console.print("[green]✓[/green] Sync data shared successfully")
                    console.print(f"[cyan]Items count:[/cyan] {data['count']}")
                    console.print(f"[cyan]For agent:[/cyan] {data['for_agent']}")
                    console.print(f"[cyan]Sync type:[/cyan] {data['sync_type']}")
                    if data['items']:
                        console.print(f"[cyan]Sample item:[/cyan] {data['items'][0].get('content', 'N/A')[:50]}...")
                    return True
                else:
                    console.print(f"[red]✗[/red] Failed with status {response.status}")
                    return False
    except Exception as e:
        console.print(f"[red]✗[/red] Error: {e}")
        return False


async def test_a2a_task_code_search():
    """Test the A2A task endpoint with code search."""
    console.print("\n[bold blue]Testing A2A Task Endpoint (Code Search)[/bold blue]")
    console.print(f"POST {MARUNOCHI_URL}/v1/a2a/task\n")

    payload = {
        "from_agent": "benchAI",
        "task_type": "code_search",
        "task_description": "find authentication functions",
        "context": {
            "knowledge": {
                "embedded_knowledge": [
                    {"content": "Looking for auth-related code"}
                ]
            }
        },
        "priority": "high"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{MARUNOCHI_URL}/v1/a2a/task",
                json=payload
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    console.print("[green]✓[/green] Task processed successfully")
                    console.print(f"[cyan]Task ID:[/cyan] {data['task_id']}")
                    console.print(f"[cyan]Status:[/cyan] {data['status']}")
                    if data.get('result'):
                        result = data['result']
                        console.print(f"[cyan]Results count:[/cyan] {result.get('count', 0)}")
                    return True
                else:
                    console.print(f"[red]✗[/red] Failed with status {response.status}")
                    text = await response.text()
                    console.print(f"[red]Response:[/red] {text}")
                    return False
    except Exception as e:
        console.print(f"[red]✗[/red] Error: {e}")
        return False


async def test_health():
    """Test the health endpoint."""
    console.print("\n[bold blue]Testing Health Endpoint[/bold blue]")
    console.print(f"GET {MARUNOCHI_URL}/health\n")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{MARUNOCHI_URL}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    console.print("[green]✓[/green] Health check passed")
                    console.print(f"[cyan]Status:[/cyan] {data['status']}")
                    console.print(f"[cyan]Ollama available:[/cyan] {data['ollama_available']}")
                    console.print(f"[cyan]Version:[/cyan] {data['version']}")
                    return True
                else:
                    console.print(f"[red]✗[/red] Failed with status {response.status}")
                    return False
    except Exception as e:
        console.print(f"[red]✗[/red] Error: {e}")
        console.print("[yellow]Note:[/yellow] Make sure MarunochiAI server is running: marunochithe server")
        return False


async def main():
    """Run all tests."""
    console.print("[bold magenta]MarunochiAI A2A Integration Tests[/bold magenta]")
    console.print("=" * 60)

    results = {
        "Health Check": await test_health(),
        "Agent Card": await test_agent_card(),
        "Sync Receive": await test_sync_receive(),
        "Sync Share": await test_sync_share(),
        "A2A Task (Code Search)": await test_a2a_task_code_search(),
    }

    # Summary table
    console.print("\n[bold magenta]Test Summary[/bold magenta]")
    console.print("=" * 60)

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Test", style="white")
    table.add_column("Result", justify="center")

    for test_name, passed in results.items():
        status = "[green]✓ PASS[/green]" if passed else "[red]✗ FAIL[/red]"
        table.add_row(test_name, status)

    console.print(table)

    # Overall result
    total = len(results)
    passed = sum(results.values())
    console.print(f"\n[bold]Results:[/bold] {passed}/{total} tests passed")

    if passed == total:
        console.print("[bold green]All tests passed! 🎉[/bold green]")
    else:
        console.print("[bold yellow]Some tests failed. Check the output above for details.[/bold yellow]")


if __name__ == "__main__":
    asyncio.run(main())
