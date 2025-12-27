#!/usr/bin/env python3
"""
Performance Benchmark Script for MarunochiAI

Tests:
- Model routing intelligence (7B vs 14B selection)
- Response latency for simple vs complex tasks
- Tokens per second throughput
- First token latency
- Code quality comparison

Based on BenchAI Hardware Optimization Report recommendations.
"""

import time
import asyncio
import aiohttp
from typing import Dict, List
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

MARUNOCHI_URL = "http://localhost:8765"


class PerformanceBenchmark:
    """Benchmark MarunochiAI performance."""

    def __init__(self):
        self.results = {}

    async def test_simple_task_7b(self) -> Dict:
        """Test simple task that should route to 7B."""
        console.print("\n[bold cyan]Testing Simple Task (Expected: 7B)[/bold cyan]")

        prompt = "Write a function to reverse a string"

        start = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{MARUNOCHI_URL}/v1/chat/completions",
                json={
                    "model": "qwen2.5-coder:7b",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False
                }
            ) as response:
                result = await response.json()
                duration = time.time() - start

        response_text = result["choices"][0]["message"]["content"]
        tokens = result["usage"]["completion_tokens"]
        tokens_per_sec = tokens / duration if duration > 0 else 0

        console.print(f"✓ Duration: {duration:.2f}s")
        console.print(f"✓ Tokens: {tokens}")
        console.print(f"✓ Tokens/sec: {tokens_per_sec:.1f}")

        return {
            "task": "simple",
            "model": "7b",
            "duration": duration,
            "tokens": tokens,
            "tokens_per_sec": tokens_per_sec,
            "response_preview": response_text[:100]
        }

    async def test_complex_task_14b(self) -> Dict:
        """Test complex task that should route to 14B."""
        console.print("\n[bold cyan]Testing Complex Task (Expected: 14B)[/bold cyan]")

        prompt = "Refactor this code to use async/await with proper error handling and type hints"

        start = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{MARUNOCHI_URL}/v1/chat/completions",
                json={
                    "model": "qwen2.5-coder:14b",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False
                }
            ) as response:
                result = await response.json()
                duration = time.time() - start

        response_text = result["choices"][0]["message"]["content"]
        tokens = result["usage"]["completion_tokens"]
        tokens_per_sec = tokens / duration if duration > 0 else 0

        console.print(f"✓ Duration: {duration:.2f}s")
        console.print(f"✓ Tokens: {tokens}")
        console.print(f"✓ Tokens/sec: {tokens_per_sec:.1f}")

        return {
            "task": "complex",
            "model": "14b",
            "duration": duration,
            "tokens": tokens,
            "tokens_per_sec": tokens_per_sec,
            "response_preview": response_text[:100]
        }

    async def test_streaming_latency(self) -> Dict:
        """Test first token latency with streaming."""
        console.print("\n[bold cyan]Testing Streaming First Token Latency[/bold cyan]")

        prompt = "Write a hello world function"

        start = time.time()
        first_token_time = None
        token_count = 0

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{MARUNOCHI_URL}/v1/chat/completions",
                json={
                    "model": "qwen2.5-coder:7b",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": True
                }
            ) as response:
                async for line in response.content:
                    if first_token_time is None and line:
                        first_token_time = time.time() - start
                        console.print(f"✓ First token: {first_token_time:.3f}s")

                    token_count += 1

        total_duration = time.time() - start
        console.print(f"✓ Total duration: {total_duration:.2f}s")
        console.print(f"✓ Chunks received: {token_count}")

        return {
            "task": "streaming",
            "model": "7b",
            "first_token_latency": first_token_time,
            "total_duration": total_duration,
            "chunks": token_count
        }

    async def test_code_quality_comparison(self) -> Dict:
        """Compare code quality between 7B and 14B."""
        console.print("\n[bold cyan]Testing Code Quality Comparison[/bold cyan]")

        prompt = "Write a Python function to implement binary search with proper error handling"

        results = {}

        for model in ["qwen2.5-coder:7b", "qwen2.5-coder:14b"]:
            model_name = "7b" if "7b" in model else "14b"
            console.print(f"\n  Testing {model_name}...")

            start = time.time()
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{MARUNOCHI_URL}/v1/chat/completions",
                    json={
                        "model": model,
                        "messages": [{"role": "user", "content": prompt}],
                        "stream": False
                    }
                ) as response:
                    result = await response.json()
                    duration = time.time() - start

            response_text = result["choices"][0]["message"]["content"]

            # Simple quality heuristics
            has_error_handling = "try" in response_text.lower() or "except" in response_text.lower()
            has_docstring = '"""' in response_text or "'''" in response_text
            has_type_hints = ":" in response_text and "->" in response_text

            quality_score = sum([has_error_handling, has_docstring, has_type_hints])

            console.print(f"    Duration: {duration:.2f}s")
            console.print(f"    Quality score: {quality_score}/3")
            console.print(f"    - Error handling: {'✓' if has_error_handling else '✗'}")
            console.print(f"    - Docstring: {'✓' if has_docstring else '✗'}")
            console.print(f"    - Type hints: {'✓' if has_type_hints else '✗'}")

            results[model_name] = {
                "duration": duration,
                "quality_score": quality_score,
                "response_length": len(response_text)
            }

        return results

    async def run_all_benchmarks(self) -> Dict:
        """Run all performance benchmarks."""
        console.print("[bold magenta]MarunochiAI Performance Benchmark[/bold magenta]")
        console.print("=" * 70)

        results = {}

        # Test 1: Simple task with 7B
        try:
            results["simple_7b"] = await self.test_simple_task_7b()
        except Exception as e:
            console.print(f"[red]Error in simple task test: {e}[/red]")
            results["simple_7b"] = {"error": str(e)}

        # Test 2: Complex task with 14B
        try:
            results["complex_14b"] = await self.test_complex_task_14b()
        except Exception as e:
            console.print(f"[red]Error in complex task test: {e}[/red]")
            results["complex_14b"] = {"error": str(e)}

        # Test 3: Streaming latency
        try:
            results["streaming"] = await self.test_streaming_latency()
        except Exception as e:
            console.print(f"[red]Error in streaming test: {e}[/red]")
            results["streaming"] = {"error": str(e)}

        # Test 4: Code quality comparison
        try:
            results["code_quality"] = await self.test_code_quality_comparison()
        except Exception as e:
            console.print(f"[red]Error in code quality test: {e}[/red]")
            results["code_quality"] = {"error": str(e)}

        # Display summary
        self._display_summary(results)

        return results

    def _display_summary(self, results: Dict):
        """Display benchmark results summary."""
        console.print("\n[bold magenta]Benchmark Summary[/bold magenta]")
        console.print("=" * 70)

        # Performance table
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Test", style="white")
        table.add_column("Model", style="yellow")
        table.add_column("Duration (s)", justify="right")
        table.add_column("Tokens/sec", justify="right")
        table.add_column("Quality", justify="center")

        if "simple_7b" in results and "error" not in results["simple_7b"]:
            r = results["simple_7b"]
            table.add_row(
                "Simple Task",
                "7B",
                f"{r['duration']:.2f}",
                f"{r['tokens_per_sec']:.1f}",
                "N/A"
            )

        if "complex_14b" in results and "error" not in results["complex_14b"]:
            r = results["complex_14b"]
            table.add_row(
                "Complex Task",
                "14B",
                f"{r['duration']:.2f}",
                f"{r['tokens_per_sec']:.1f}",
                "N/A"
            )

        if "streaming" in results and "error" not in results["streaming"]:
            r = results["streaming"]
            table.add_row(
                "Streaming",
                "7B",
                f"{r.get('total_duration', 0):.2f}",
                f"TTFT: {r.get('first_token_latency', 0):.3f}s",
                "N/A"
            )

        if "code_quality" in results and "error" not in results["code_quality"]:
            for model, data in results["code_quality"].items():
                table.add_row(
                    "Code Quality",
                    model.upper(),
                    f"{data['duration']:.2f}",
                    "N/A",
                    f"{data['quality_score']}/3"
                )

        console.print(table)

        # Recommendations
        console.print("\n[bold yellow]Optimization Recommendations:[/bold yellow]")

        if "streaming" in results and "first_token_latency" in results["streaming"]:
            ttft = results["streaming"]["first_token_latency"]
            if ttft > 2.0:
                console.print(f"⚠️  First token latency is {ttft:.2f}s (target: <1s)")
                console.print("   Consider: Model quantization or faster inference backend")
            else:
                console.print(f"✓ First token latency is good: {ttft:.2f}s")

        if "simple_7b" in results and "tokens_per_sec" in results["simple_7b"]:
            tps = results["simple_7b"]["tokens_per_sec"]
            if tps < 30:
                console.print(f"⚠️  7B throughput is {tps:.1f} tok/s (target: >40)")
                console.print("   Consider: Checking M4 Pro GPU utilization")
            else:
                console.print(f"✓ 7B throughput is good: {tps:.1f} tok/s")

        console.print("\n[bold green]Benchmark Complete![/bold green]")


async def main():
    """Run performance benchmarks."""
    benchmark = PerformanceBenchmark()

    # Check server health first
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{MARUNOCHI_URL}/health") as response:
                health = await response.json()
                console.print(f"[green]✓[/green] MarunochiAI server is running (v{health['version']})")
    except Exception as e:
        console.print(f"[red]✗ Cannot connect to MarunochiAI server: {e}[/red]")
        console.print("  Make sure the server is running: marunochithe server")
        return

    # Run benchmarks
    results = await benchmark.run_all_benchmarks()

    # Save results
    import json
    with open("/tmp/marunochiAI_benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)

    console.print(f"\n[dim]Results saved to: /tmp/marunochiAI_benchmark_results.json[/dim]")


if __name__ == "__main__":
    asyncio.run(main())
