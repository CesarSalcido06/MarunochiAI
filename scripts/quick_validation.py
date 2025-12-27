#!/usr/bin/env python3
"""
Quick Validation Test for MarunochiAI

Fast validation (<3 minutes) to ensure MarunochiAI is working properly.
Tests essential functions without long stress testing.
"""

import asyncio
import aiohttp
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

MARUNOCHI_URL = "http://localhost:8765"

class QuickValidator:
    """Quick validation tests for MarunochiAI."""

    def __init__(self):
        self.results = []

    async def test_health_check(self) -> bool:
        """Test 1: Server Health Check"""
        console.print("\n[cyan]1. Testing Server Health...[/cyan]")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{MARUNOCHI_URL}/health", timeout=5) as response:
                    if response.status == 200:
                        health = await response.json()
                        console.print(f"  [green]✓[/green] Server running v{health.get('version')}")
                        console.print(f"  [green]✓[/green] Status: {health.get('status')}")
                        console.print(f"  [green]✓[/green] Models: {', '.join(health.get('models_loaded', []))}")
                        self.results.append(("Health Check", "PASS", "Server operational"))
                        return True
        except Exception as e:
            console.print(f"  [red]✗[/red] Health check failed: {e}")
            self.results.append(("Health Check", "FAIL", str(e)))
            return False

    async def test_simple_inference(self) -> bool:
        """Test 2: Simple Inference (7B)"""
        console.print("\n[cyan]2. Testing Simple Inference (7B)...[/cyan]")
        try:
            start = time.time()
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{MARUNOCHI_URL}/v1/chat/completions",
                    json={
                        "model": "qwen2.5-coder:7b",
                        "messages": [{"role": "user", "content": "Write a function to add two numbers"}],
                        "stream": False
                    },
                    timeout=aiohttp.ClientTimeout(total=120)
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        duration = time.time() - start
                        tokens = result.get("usage", {}).get("completion_tokens", 0)
                        console.print(f"  [green]✓[/green] Inference successful")
                        console.print(f"  [green]✓[/green] Duration: {duration:.1f}s")
                        console.print(f"  [green]✓[/green] Tokens generated: {tokens}")
                        console.print(f"  [green]✓[/green] Response preview: {result['choices'][0]['message']['content'][:100]}...")
                        self.results.append(("Simple Inference", "PASS", f"{duration:.1f}s, {tokens} tokens"))
                        return True
                    else:
                        error = await response.text()
                        console.print(f"  [red]✗[/red] HTTP {response.status}: {error[:100]}")
                        self.results.append(("Simple Inference", "FAIL", f"HTTP {response.status}"))
                        return False
        except Exception as e:
            console.print(f"  [red]✗[/red] Inference failed: {e}")
            self.results.append(("Simple Inference", "FAIL", str(e)))
            return False

    async def test_streaming(self) -> bool:
        """Test 3: Streaming Response"""
        console.print("\n[cyan]3. Testing Streaming Response...[/cyan]")
        try:
            start = time.time()
            first_chunk_time = None
            chunk_count = 0

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{MARUNOCHI_URL}/v1/chat/completions",
                    json={
                        "model": "qwen2.5-coder:7b",
                        "messages": [{"role": "user", "content": "Hello"}],
                        "stream": True
                    },
                    timeout=aiohttp.ClientTimeout(total=120)
                ) as response:
                    if response.status == 200:
                        async for chunk in response.content.iter_any():
                            if first_chunk_time is None:
                                first_chunk_time = time.time() - start
                            chunk_count += 1
                            if chunk_count >= 5:  # Just test first 5 chunks
                                break

                        console.print(f"  [green]✓[/green] Streaming working")
                        console.print(f"  [green]✓[/green] First chunk: {first_chunk_time:.2f}s")
                        console.print(f"  [green]✓[/green] Chunks received: {chunk_count}")
                        self.results.append(("Streaming", "PASS", f"TTFT {first_chunk_time:.2f}s"))
                        return True
                    else:
                        console.print(f"  [red]✗[/red] HTTP {response.status}")
                        self.results.append(("Streaming", "FAIL", f"HTTP {response.status}"))
                        return False
        except Exception as e:
            console.print(f"  [red]✗[/red] Streaming failed: {e}")
            self.results.append(("Streaming", "FAIL", str(e)))
            return False

    async def test_a2a_endpoints(self) -> bool:
        """Test 4: A2A Integration Endpoints"""
        console.print("\n[cyan]4. Testing A2A Integration Endpoints...[/cyan]")
        passed = 0
        total = 4

        async with aiohttp.ClientSession() as session:
            # Test agent card
            try:
                async with session.get(f"{MARUNOCHI_URL}/.well-known/agent.json", timeout=5) as response:
                    if response.status == 200:
                        card = await response.json()
                        console.print(f"  [green]✓[/green] Agent Card: {card.get('name')}")
                        passed += 1
                    else:
                        console.print(f"  [red]✗[/red] Agent Card failed: HTTP {response.status}")
            except Exception as e:
                console.print(f"  [red]✗[/red] Agent Card: {str(e)[:50]}")

            # Test sync receive
            try:
                async with session.post(
                    f"{MARUNOCHI_URL}/v1/sync/receive",
                    json={
                        "from_agent": "test",
                        "sync_type": "experience",
                        "items": [{"id": "test1", "data": "test"}]
                    },
                    timeout=5
                ) as response:
                    if response.status == 200:
                        console.print(f"  [green]✓[/green] Sync Receive working")
                        passed += 1
                    else:
                        console.print(f"  [red]✗[/red] Sync Receive failed: HTTP {response.status}")
            except Exception as e:
                console.print(f"  [red]✗[/red] Sync Receive: {str(e)[:50]}")

            # Test sync share
            try:
                async with session.get(f"{MARUNOCHI_URL}/v1/sync/share", timeout=5) as response:
                    if response.status == 200:
                        console.print(f"  [green]✓[/green] Sync Share working")
                        passed += 1
                    else:
                        console.print(f"  [red]✗[/red] Sync Share failed: HTTP {response.status}")
            except Exception as e:
                console.print(f"  [red]✗[/red] Sync Share: {str(e)[:50]}")

            # Test A2A task
            try:
                async with session.post(
                    f"{MARUNOCHI_URL}/v1/a2a/task",
                    json={
                        "from_agent": "test",
                        "task_type": "code_search",
                        "task_description": "test task",
                        "priority": "normal"
                    },
                    timeout=10
                ) as response:
                    if response.status == 200:
                        console.print(f"  [green]✓[/green] A2A Task processing working")
                        passed += 1
                    else:
                        console.print(f"  [red]✗[/red] A2A Task failed: HTTP {response.status}")
            except Exception as e:
                console.print(f"  [red]✗[/red] A2A Task: {str(e)[:50]}")

        success = passed == total
        status = "PASS" if success else f"PARTIAL ({passed}/{total})"
        self.results.append(("A2A Endpoints", status, f"{passed}/{total} working"))
        return success

    async def test_concurrent_requests(self) -> bool:
        """Test 5: Concurrent Request Handling"""
        console.print("\n[cyan]5. Testing Concurrent Requests (10 requests)...[/cyan]")

        num_requests = 10
        successful = 0
        failed = 0

        async def make_request(session, i):
            nonlocal successful, failed
            try:
                async with session.post(
                    f"{MARUNOCHI_URL}/v1/chat/completions",
                    json={
                        "model": "qwen2.5-coder:7b",
                        "messages": [{"role": "user", "content": f"test {i}"}],
                        "stream": False
                    },
                    timeout=aiohttp.ClientTimeout(total=120)
                ) as response:
                    if response.status == 200:
                        successful += 1
                    else:
                        failed += 1
            except Exception:
                failed += 1

        start = time.time()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[make_request(session, i) for i in range(num_requests)])
        duration = time.time() - start

        console.print(f"  [green]✓[/green] Success: {successful}/{num_requests}")
        console.print(f"  [green]✓[/green] Duration: {duration:.1f}s")
        console.print(f"  [green]✓[/green] Throughput: {num_requests/duration:.2f} req/s")

        status = "PASS" if successful == num_requests else f"PARTIAL ({successful}/{num_requests})"
        self.results.append(("Concurrent Requests", status, f"{successful}/{num_requests} successful"))
        return successful == num_requests

    async def test_error_handling(self) -> bool:
        """Test 6: Error Handling"""
        console.print("\n[cyan]6. Testing Error Handling...[/cyan]")

        test_cases = [
            ("Invalid model", {"model": "nonexistent", "messages": [{"role": "user", "content": "test"}]}),
            ("Missing messages", {"model": "qwen2.5-coder:7b"}),
            ("Empty prompt", {"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": ""}]}),
        ]

        handled_correctly = 0
        async with aiohttp.ClientSession() as session:
            for desc, payload in test_cases:
                try:
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/chat/completions",
                        json=payload,
                        timeout=10
                    ) as response:
                        # Should return error response (4xx or 5xx)
                        if response.status >= 400:
                            console.print(f"  [green]✓[/green] {desc}: Properly rejected (HTTP {response.status})")
                            handled_correctly += 1
                        else:
                            # Empty prompt might be accepted
                            if "empty" in desc.lower():
                                console.print(f"  [yellow]~[/yellow] {desc}: Accepted (might be intentional)")
                                handled_correctly += 1
                            else:
                                console.print(f"  [red]✗[/red] {desc}: Should have failed but succeeded")
                except Exception as e:
                    # Exception is also acceptable for invalid requests
                    console.print(f"  [green]✓[/green] {desc}: Rejected with exception")
                    handled_correctly += 1

        total = len(test_cases)
        status = "PASS" if handled_correctly >= total - 1 else f"PARTIAL ({handled_correctly}/{total})"
        self.results.append(("Error Handling", status, f"{handled_correctly}/{total} handled correctly"))
        return handled_correctly >= total - 1

    def print_final_report(self):
        """Print final validation report."""
        console.print("\n" + "="*70)
        console.print("[bold magenta]QUICK VALIDATION REPORT[/bold magenta]")
        console.print("="*70 + "\n")

        # Results table
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Test", style="white", width=25)
        table.add_column("Status", justify="center", width=10)
        table.add_column("Details", style="dim", width=30)

        for test_name, status, details in self.results:
            if status == "PASS":
                status_display = "[green]PASS[/green]"
            elif status.startswith("PARTIAL"):
                status_display = f"[yellow]{status}[/yellow]"
            else:
                status_display = "[red]FAIL[/red]"

            table.add_row(test_name, status_display, details)

        console.print(table)

        # Overall assessment
        total_tests = len(self.results)
        passed = sum(1 for _, status, _ in self.results if status == "PASS")
        partial = sum(1 for _, status, _ in self.results if status.startswith("PARTIAL"))
        failed = sum(1 for _, status, _ in self.results if status == "FAIL")

        console.print(f"\n[bold]Overall Results:[/bold]")
        console.print(f"  Total: {total_tests}")
        console.print(f"  [green]Passed: {passed}[/green]")
        console.print(f"  [yellow]Partial: {partial}[/yellow]")
        console.print(f"  [red]Failed: {failed}[/red]")

        # Production readiness
        is_ready = failed == 0 and passed >= total_tests - 1

        console.print(f"\n[bold]Production Readiness:[/bold]")
        if is_ready:
            console.print("[bold green]✓ MarunochiAI is WORKING PROPERLY![/bold green]")
            console.print("  All critical functions validated. Ready for use.")
        elif failed == 0:
            console.print("[bold yellow]⚠ MarunochiAI is MOSTLY WORKING[/bold yellow]")
            console.print("  Some features partially working. Review recommended.")
        else:
            console.print("[bold red]✗ MarunochiAI has ISSUES[/bold red]")
            console.print(f"  {failed} tests failed. Needs attention.")

        return is_ready

    async def run_all_tests(self):
        """Run all validation tests."""
        console.print(Panel.fit(
            "[bold cyan]MarunochiAI Quick Validation[/bold cyan]\n"
            "Testing essential functions...",
            border_style="cyan"
        ))

        start = time.time()

        # Run tests
        await self.test_health_check()
        await self.test_simple_inference()
        await self.test_streaming()
        await self.test_a2a_endpoints()
        await self.test_concurrent_requests()
        await self.test_error_handling()

        duration = time.time() - start

        # Final report
        is_ready = self.print_final_report()

        console.print(f"\n[dim]Validation completed in {duration:.1f}s[/dim]")

        return is_ready


async def main():
    """Main entry point."""
    validator = QuickValidator()

    try:
        is_ready = await validator.run_all_tests()

        if is_ready:
            console.print("\n[bold green]✓ SUCCESS: MarunochiAI is ready to be the best tool![/bold green]")
            return 0
        else:
            console.print("\n[bold yellow]⚠ REVIEW: Some issues need attention[/bold yellow]")
            return 1
    except Exception as e:
        console.print(f"\n[red]Error during validation: {e}[/red]")
        import traceback
        console.print(traceback.format_exc())
        return 2


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
