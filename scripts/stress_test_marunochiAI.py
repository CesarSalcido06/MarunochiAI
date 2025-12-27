#!/usr/bin/env python3
"""
Comprehensive Stress Test Suite for MarunochiAI

Tests production readiness with:
- Load testing (concurrent requests)
- Edge cases (malformed requests, large prompts)
- Integration stress (A2A tasks, sync operations)
- Resource monitoring (memory, latency distribution)
- Error handling and recovery
- Long-running stability

Goal: Ensure MarunochiAI is ready to be "the best tool"
"""

import asyncio
import aiohttp
import time
import json
import statistics
import psutil
import traceback
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout

console = Console()

MARUNOCHI_URL = "http://localhost:8765"
BENCHAI_URL = "http://localhost:8085"

@dataclass
class StressTestResult:
    """Result from a stress test scenario."""
    test_name: str
    total_requests: int
    successful_requests: int
    failed_requests: int
    avg_latency_ms: float
    p50_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    max_latency_ms: float
    min_latency_ms: float
    requests_per_second: float
    error_rate: float
    errors: List[str]
    memory_usage_mb: float
    duration_seconds: float
    status: str  # "PASS", "FAIL", "WARN"

@dataclass
class SystemMetrics:
    """System resource metrics during test."""
    timestamp: float
    cpu_percent: float
    memory_percent: float
    memory_used_mb: float
    available_memory_mb: float


class StressTestSuite:
    """Comprehensive stress testing for MarunochiAI."""

    def __init__(self):
        self.results: List[StressTestResult] = []
        self.system_metrics: List[SystemMetrics] = []
        self.process = psutil.Process()

    async def check_server_health(self) -> bool:
        """Verify server is running before tests."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{MARUNOCHI_URL}/health", timeout=5) as response:
                    if response.status == 200:
                        health = await response.json()
                        console.print(f"[green]✓[/green] MarunochiAI server running (v{health.get('version', 'unknown')})")
                        return True
        except Exception as e:
            console.print(f"[red]✗[/red] Cannot connect to MarunochiAI server: {e}")
            console.print("  Start server with: marunochithe server")
            return False
        return False

    async def collect_system_metrics(self):
        """Continuously collect system metrics during tests."""
        while True:
            try:
                metrics = SystemMetrics(
                    timestamp=time.time(),
                    cpu_percent=self.process.cpu_percent(),
                    memory_percent=self.process.memory_percent(),
                    memory_used_mb=self.process.memory_info().rss / 1024 / 1024,
                    available_memory_mb=psutil.virtual_memory().available / 1024 / 1024
                )
                self.system_metrics.append(metrics)
                await asyncio.sleep(1)
            except asyncio.CancelledError:
                break
            except Exception as e:
                console.print(f"[yellow]Warning: Metrics collection error: {e}[/yellow]")
                await asyncio.sleep(1)

    async def run_concurrent_requests(
        self,
        num_requests: int = 50,
        concurrent_limit: int = 10,
        test_name: str = "Concurrent Load Test"
    ) -> StressTestResult:
        """
        Test 1: Concurrent Request Load

        Simulates multiple users making requests simultaneously.
        """
        console.print(f"\n[bold cyan]Running: {test_name}[/bold cyan]")
        console.print(f"  Requests: {num_requests}, Concurrency: {concurrent_limit}")

        latencies = []
        errors = []
        successful = 0
        failed = 0

        start_time = time.time()
        start_memory = self.process.memory_info().rss / 1024 / 1024

        semaphore = asyncio.Semaphore(concurrent_limit)

        async def make_request(session: aiohttp.ClientSession, request_id: int):
            nonlocal successful, failed

            async with semaphore:
                req_start = time.time()
                try:
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/chat/completions",
                        json={
                            "model": "qwen2.5-coder:7b",
                            "messages": [{
                                "role": "user",
                                "content": f"Write a function to calculate fibonacci number {request_id}"
                            }],
                            "stream": False
                        },
                        timeout=aiohttp.ClientTimeout(total=60)
                    ) as response:
                        await response.json()
                        latency = (time.time() - req_start) * 1000
                        latencies.append(latency)
                        successful += 1
                except Exception as e:
                    latency = (time.time() - req_start) * 1000
                    latencies.append(latency)
                    failed += 1
                    errors.append(f"Request {request_id}: {str(e)[:100]}")

        async with aiohttp.ClientSession() as session:
            tasks = [make_request(session, i) for i in range(num_requests)]

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=console
            ) as progress:
                task = progress.add_task(f"Processing {num_requests} requests...", total=num_requests)

                for coro in asyncio.as_completed(tasks):
                    await coro
                    progress.advance(task)

        end_time = time.time()
        end_memory = self.process.memory_info().rss / 1024 / 1024
        duration = end_time - start_time

        # Calculate statistics
        if latencies:
            result = StressTestResult(
                test_name=test_name,
                total_requests=num_requests,
                successful_requests=successful,
                failed_requests=failed,
                avg_latency_ms=statistics.mean(latencies),
                p50_latency_ms=statistics.median(latencies),
                p95_latency_ms=statistics.quantiles(latencies, n=20)[18] if len(latencies) > 1 else latencies[0],
                p99_latency_ms=statistics.quantiles(latencies, n=100)[98] if len(latencies) > 1 else latencies[0],
                max_latency_ms=max(latencies),
                min_latency_ms=min(latencies),
                requests_per_second=num_requests / duration,
                error_rate=failed / num_requests,
                errors=errors[:10],  # Keep first 10 errors
                memory_usage_mb=end_memory - start_memory,
                duration_seconds=duration,
                status="PASS" if failed / num_requests < 0.05 else "FAIL"
            )
        else:
            result = StressTestResult(
                test_name=test_name,
                total_requests=num_requests,
                successful_requests=0,
                failed_requests=num_requests,
                avg_latency_ms=0,
                p50_latency_ms=0,
                p95_latency_ms=0,
                p99_latency_ms=0,
                max_latency_ms=0,
                min_latency_ms=0,
                requests_per_second=0,
                error_rate=1.0,
                errors=errors[:10],
                memory_usage_mb=end_memory - start_memory,
                duration_seconds=duration,
                status="FAIL"
            )

        self._print_result_summary(result)
        self.results.append(result)
        return result

    async def test_edge_cases(self) -> StressTestResult:
        """
        Test 2: Edge Case Handling

        Tests malformed requests, very long prompts, invalid inputs.
        """
        console.print("\n[bold cyan]Running: Edge Case Testing[/bold cyan]")

        test_cases = [
            # (description, request_payload, should_fail)
            ("Empty prompt", {"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": ""}]}, False),
            ("Very long prompt", {"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": "x" * 10000}]}, False),
            ("Invalid model", {"model": "nonexistent-model", "messages": [{"role": "user", "content": "test"}]}, True),
            ("Missing messages", {"model": "qwen2.5-coder:7b"}, True),
            ("Invalid message format", {"model": "qwen2.5-coder:7b", "messages": "not a list"}, True),
            ("Special characters", {"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": "Test\n\t\r\x00Special"}]}, False),
            ("Unicode emoji", {"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": "Write code 🚀💻🎉"}]}, False),
            ("Very nested JSON", {"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": json.dumps({"a": {"b": {"c": {"d": "test"}}}})}]}, False),
        ]

        latencies = []
        errors = []
        successful = 0
        failed = 0

        start_time = time.time()
        start_memory = self.process.memory_info().rss / 1024 / 1024

        async with aiohttp.ClientSession() as session:
            for desc, payload, should_fail in test_cases:
                req_start = time.time()
                try:
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/chat/completions",
                        json=payload,
                        timeout=aiohttp.ClientTimeout(total=30)
                    ) as response:
                        latency = (time.time() - req_start) * 1000
                        latencies.append(latency)

                        if response.status >= 400 and not should_fail:
                            failed += 1
                            errors.append(f"{desc}: Unexpected error {response.status}")
                        elif response.status < 400 and should_fail:
                            failed += 1
                            errors.append(f"{desc}: Should have failed but succeeded")
                        else:
                            successful += 1
                            console.print(f"  [green]✓[/green] {desc}")
                except Exception as e:
                    latency = (time.time() - req_start) * 1000
                    latencies.append(latency)

                    if should_fail:
                        successful += 1
                        console.print(f"  [green]✓[/green] {desc} (expected failure)")
                    else:
                        failed += 1
                        errors.append(f"{desc}: {str(e)[:100]}")
                        console.print(f"  [red]✗[/red] {desc}: {str(e)[:50]}")

        end_time = time.time()
        end_memory = self.process.memory_info().rss / 1024 / 1024
        duration = end_time - start_time

        num_tests = len(test_cases)
        result = StressTestResult(
            test_name="Edge Case Testing",
            total_requests=num_tests,
            successful_requests=successful,
            failed_requests=failed,
            avg_latency_ms=statistics.mean(latencies) if latencies else 0,
            p50_latency_ms=statistics.median(latencies) if latencies else 0,
            p95_latency_ms=statistics.quantiles(latencies, n=20)[18] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            p99_latency_ms=statistics.quantiles(latencies, n=100)[98] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            max_latency_ms=max(latencies) if latencies else 0,
            min_latency_ms=min(latencies) if latencies else 0,
            requests_per_second=num_tests / duration if duration > 0 else 0,
            error_rate=failed / num_tests if num_tests > 0 else 0,
            errors=errors,
            memory_usage_mb=end_memory - start_memory,
            duration_seconds=duration,
            status="PASS" if failed == 0 else "WARN"
        )

        self._print_result_summary(result)
        self.results.append(result)
        return result

    async def test_a2a_integration_stress(self) -> StressTestResult:
        """
        Test 3: A2A Integration Stress

        Rapid A2A task submissions and sync operations.
        """
        console.print("\n[bold cyan]Running: A2A Integration Stress Test[/bold cyan]")

        num_tasks = 30
        latencies = []
        errors = []
        successful = 0
        failed = 0

        start_time = time.time()
        start_memory = self.process.memory_info().rss / 1024 / 1024

        async with aiohttp.ClientSession() as session:
            # Test rapid A2A task submissions
            for i in range(num_tasks):
                req_start = time.time()
                try:
                    # A2A task endpoint
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/a2a/task",
                        json={
                            "from_agent": "stress_test",
                            "task_type": "code_search",
                            "task_description": f"Find authentication functions test {i}",
                            "priority": "normal"
                        },
                        timeout=aiohttp.ClientTimeout(total=30)
                    ) as response:
                        latency = (time.time() - req_start) * 1000
                        latencies.append(latency)

                        if response.status == 200:
                            successful += 1
                        else:
                            failed += 1
                            errors.append(f"A2A task {i}: HTTP {response.status}")
                except Exception as e:
                    latency = (time.time() - req_start) * 1000
                    latencies.append(latency)
                    failed += 1
                    errors.append(f"A2A task {i}: {str(e)[:100]}")

            # Test sync endpoints
            for sync_type in ["experience", "knowledge"]:
                req_start = time.time()
                try:
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/sync/receive",
                        json={
                            "from_agent": "stress_test",
                            "sync_type": sync_type,
                            "items": [
                                {"id": f"test_{i}", "data": f"Test data {i}"}
                                for i in range(5)
                            ]
                        },
                        timeout=aiohttp.ClientTimeout(total=10)
                    ) as response:
                        latency = (time.time() - req_start) * 1000
                        latencies.append(latency)

                        if response.status == 200:
                            successful += 1
                        else:
                            failed += 1
                            errors.append(f"Sync {sync_type}: HTTP {response.status}")
                except Exception as e:
                    latency = (time.time() - req_start) * 1000
                    latencies.append(latency)
                    failed += 1
                    errors.append(f"Sync {sync_type}: {str(e)[:100]}")

        end_time = time.time()
        end_memory = self.process.memory_info().rss / 1024 / 1024
        duration = end_time - start_time

        total_requests = num_tasks + 2  # tasks + 2 sync types
        result = StressTestResult(
            test_name="A2A Integration Stress",
            total_requests=total_requests,
            successful_requests=successful,
            failed_requests=failed,
            avg_latency_ms=statistics.mean(latencies) if latencies else 0,
            p50_latency_ms=statistics.median(latencies) if latencies else 0,
            p95_latency_ms=statistics.quantiles(latencies, n=20)[18] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            p99_latency_ms=statistics.quantiles(latencies, n=100)[98] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            max_latency_ms=max(latencies) if latencies else 0,
            min_latency_ms=min(latencies) if latencies else 0,
            requests_per_second=total_requests / duration if duration > 0 else 0,
            error_rate=failed / total_requests if total_requests > 0 else 0,
            errors=errors[:10],
            memory_usage_mb=end_memory - start_memory,
            duration_seconds=duration,
            status="PASS" if failed / total_requests < 0.1 else "FAIL"
        )

        self._print_result_summary(result)
        self.results.append(result)
        return result

    async def test_streaming_stability(self) -> StressTestResult:
        """
        Test 4: Streaming Response Stability

        Tests streaming responses for stability and error handling.
        """
        console.print("\n[bold cyan]Running: Streaming Stability Test[/bold cyan]")

        num_streams = 20
        latencies = []
        errors = []
        successful = 0
        failed = 0

        start_time = time.time()
        start_memory = self.process.memory_info().rss / 1024 / 1024

        async with aiohttp.ClientSession() as session:
            for i in range(num_streams):
                req_start = time.time()
                chunk_count = 0
                first_chunk_time = None

                try:
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/chat/completions",
                        json={
                            "model": "qwen2.5-coder:7b",
                            "messages": [{
                                "role": "user",
                                "content": f"Write a function to process data {i}"
                            }],
                            "stream": True
                        },
                        timeout=aiohttp.ClientTimeout(total=60)
                    ) as response:
                        async for chunk in response.content.iter_any():
                            if first_chunk_time is None:
                                first_chunk_time = time.time() - req_start
                            chunk_count += 1

                        latency = (time.time() - req_start) * 1000
                        latencies.append(latency)

                        if chunk_count > 0:
                            successful += 1
                        else:
                            failed += 1
                            errors.append(f"Stream {i}: No chunks received")
                except Exception as e:
                    latency = (time.time() - req_start) * 1000
                    latencies.append(latency)
                    failed += 1
                    errors.append(f"Stream {i}: {str(e)[:100]}")

        end_time = time.time()
        end_memory = self.process.memory_info().rss / 1024 / 1024
        duration = end_time - start_time

        result = StressTestResult(
            test_name="Streaming Stability",
            total_requests=num_streams,
            successful_requests=successful,
            failed_requests=failed,
            avg_latency_ms=statistics.mean(latencies) if latencies else 0,
            p50_latency_ms=statistics.median(latencies) if latencies else 0,
            p95_latency_ms=statistics.quantiles(latencies, n=20)[18] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            p99_latency_ms=statistics.quantiles(latencies, n=100)[98] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            max_latency_ms=max(latencies) if latencies else 0,
            min_latency_ms=min(latencies) if latencies else 0,
            requests_per_second=num_streams / duration if duration > 0 else 0,
            error_rate=failed / num_streams if num_streams > 0 else 0,
            errors=errors[:10],
            memory_usage_mb=end_memory - start_memory,
            duration_seconds=duration,
            status="PASS" if failed / num_streams < 0.05 else "FAIL"
        )

        self._print_result_summary(result)
        self.results.append(result)
        return result

    async def test_rapid_model_switching(self) -> StressTestResult:
        """
        Test 5: Rapid Model Switching

        Tests switching between 7B and 14B models rapidly.
        """
        console.print("\n[bold cyan]Running: Rapid Model Switching Test[/bold cyan]")

        num_switches = 20
        latencies = []
        errors = []
        successful = 0
        failed = 0

        start_time = time.time()
        start_memory = self.process.memory_info().rss / 1024 / 1024

        async with aiohttp.ClientSession() as session:
            for i in range(num_switches):
                model = "qwen2.5-coder:7b" if i % 2 == 0 else "qwen2.5-coder:14b"
                req_start = time.time()

                try:
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/chat/completions",
                        json={
                            "model": model,
                            "messages": [{
                                "role": "user",
                                "content": f"Quick test {i}"
                            }],
                            "stream": False
                        },
                        timeout=aiohttp.ClientTimeout(total=60)
                    ) as response:
                        await response.json()
                        latency = (time.time() - req_start) * 1000
                        latencies.append(latency)
                        successful += 1
                except Exception as e:
                    latency = (time.time() - req_start) * 1000
                    latencies.append(latency)
                    failed += 1
                    errors.append(f"Switch {i} ({model}): {str(e)[:100]}")

        end_time = time.time()
        end_memory = self.process.memory_info().rss / 1024 / 1024
        duration = end_time - start_time

        result = StressTestResult(
            test_name="Rapid Model Switching",
            total_requests=num_switches,
            successful_requests=successful,
            failed_requests=failed,
            avg_latency_ms=statistics.mean(latencies) if latencies else 0,
            p50_latency_ms=statistics.median(latencies) if latencies else 0,
            p95_latency_ms=statistics.quantiles(latencies, n=20)[18] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            p99_latency_ms=statistics.quantiles(latencies, n=100)[98] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            max_latency_ms=max(latencies) if latencies else 0,
            min_latency_ms=min(latencies) if latencies else 0,
            requests_per_second=num_switches / duration if duration > 0 else 0,
            error_rate=failed / num_switches if num_switches > 0 else 0,
            errors=errors[:10],
            memory_usage_mb=end_memory - start_memory,
            duration_seconds=duration,
            status="PASS" if failed / num_switches < 0.05 else "FAIL"
        )

        self._print_result_summary(result)
        self.results.append(result)
        return result

    async def test_memory_leak(self) -> StressTestResult:
        """
        Test 6: Memory Leak Detection

        Runs sustained load to detect memory leaks.
        """
        console.print("\n[bold cyan]Running: Memory Leak Detection (60s sustained load)[/bold cyan]")

        duration_seconds = 60
        latencies = []
        errors = []
        successful = 0
        failed = 0
        memory_samples = []

        start_time = time.time()
        start_memory = self.process.memory_info().rss / 1024 / 1024
        memory_samples.append(start_memory)

        request_count = 0

        async with aiohttp.ClientSession() as session:
            while time.time() - start_time < duration_seconds:
                req_start = time.time()
                request_count += 1

                try:
                    async with session.post(
                        f"{MARUNOCHI_URL}/v1/chat/completions",
                        json={
                            "model": "qwen2.5-coder:7b",
                            "messages": [{
                                "role": "user",
                                "content": f"Test request {request_count}"
                            }],
                            "stream": False
                        },
                        timeout=aiohttp.ClientTimeout(total=30)
                    ) as response:
                        await response.json()
                        latency = (time.time() - req_start) * 1000
                        latencies.append(latency)
                        successful += 1

                        # Sample memory every 10 requests
                        if request_count % 10 == 0:
                            current_memory = self.process.memory_info().rss / 1024 / 1024
                            memory_samples.append(current_memory)
                except Exception as e:
                    latency = (time.time() - req_start) * 1000
                    latencies.append(latency)
                    failed += 1
                    errors.append(f"Request {request_count}: {str(e)[:100]}")

        end_time = time.time()
        end_memory = self.process.memory_info().rss / 1024 / 1024
        duration = end_time - start_time

        # Analyze memory trend
        memory_increase = end_memory - start_memory
        memory_growth_rate = memory_increase / duration  # MB per second

        # If memory grows > 5MB/min, might be a leak
        leak_detected = memory_growth_rate > (5.0 / 60)

        result = StressTestResult(
            test_name="Memory Leak Detection",
            total_requests=request_count,
            successful_requests=successful,
            failed_requests=failed,
            avg_latency_ms=statistics.mean(latencies) if latencies else 0,
            p50_latency_ms=statistics.median(latencies) if latencies else 0,
            p95_latency_ms=statistics.quantiles(latencies, n=20)[18] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            p99_latency_ms=statistics.quantiles(latencies, n=100)[98] if len(latencies) > 1 else (latencies[0] if latencies else 0),
            max_latency_ms=max(latencies) if latencies else 0,
            min_latency_ms=min(latencies) if latencies else 0,
            requests_per_second=request_count / duration if duration > 0 else 0,
            error_rate=failed / request_count if request_count > 0 else 0,
            errors=errors[:10],
            memory_usage_mb=memory_increase,
            duration_seconds=duration,
            status="WARN" if leak_detected else "PASS"
        )

        console.print(f"\n  Memory samples: {len(memory_samples)}")
        console.print(f"  Start memory: {start_memory:.1f} MB")
        console.print(f"  End memory: {end_memory:.1f} MB")
        console.print(f"  Memory increase: {memory_increase:.1f} MB")
        console.print(f"  Growth rate: {memory_growth_rate * 60:.2f} MB/min")
        if leak_detected:
            console.print(f"  [yellow]⚠️  Possible memory leak detected[/yellow]")
        else:
            console.print(f"  [green]✓ No memory leak detected[/green]")

        self._print_result_summary(result)
        self.results.append(result)
        return result

    def _print_result_summary(self, result: StressTestResult):
        """Print summary of a single test result."""
        status_color = {
            "PASS": "green",
            "WARN": "yellow",
            "FAIL": "red"
        }

        color = status_color.get(result.status, "white")
        console.print(f"\n[{color}]{result.status}[/{color}] {result.test_name}")
        console.print(f"  Success: {result.successful_requests}/{result.total_requests} "
                     f"({result.successful_requests/result.total_requests*100:.1f}%)")
        console.print(f"  Latency: avg={result.avg_latency_ms:.0f}ms, "
                     f"p95={result.p95_latency_ms:.0f}ms, "
                     f"max={result.max_latency_ms:.0f}ms")
        console.print(f"  Throughput: {result.requests_per_second:.2f} req/s")

        if result.errors:
            console.print(f"  [yellow]Errors ({len(result.errors)}):[/yellow]")
            for error in result.errors[:3]:
                console.print(f"    - {error}")

    def generate_final_report(self) -> str:
        """Generate comprehensive final report."""
        console.print("\n" + "="*70)
        console.print("[bold magenta]STRESS TEST FINAL REPORT[/bold magenta]")
        console.print("="*70)

        # Summary table
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Test", style="white")
        table.add_column("Status", justify="center")
        table.add_column("Success Rate", justify="right")
        table.add_column("Avg Latency", justify="right")
        table.add_column("P95 Latency", justify="right")
        table.add_column("Throughput", justify="right")

        for result in self.results:
            status_emoji = {
                "PASS": "[green]✓[/green]",
                "WARN": "[yellow]⚠[/yellow]",
                "FAIL": "[red]✗[/red]"
            }

            table.add_row(
                result.test_name[:30],
                status_emoji.get(result.status, "?"),
                f"{result.successful_requests/result.total_requests*100:.1f}%",
                f"{result.avg_latency_ms:.0f}ms",
                f"{result.p95_latency_ms:.0f}ms",
                f"{result.requests_per_second:.1f}/s"
            )

        console.print(table)

        # Overall assessment
        total_tests = len(self.results)
        passed = sum(1 for r in self.results if r.status == "PASS")
        warnings = sum(1 for r in self.results if r.status == "WARN")
        failed = sum(1 for r in self.results if r.status == "FAIL")

        console.print(f"\n[bold]Overall Results:[/bold]")
        console.print(f"  Total tests: {total_tests}")
        console.print(f"  [green]Passed: {passed}[/green]")
        console.print(f"  [yellow]Warnings: {warnings}[/yellow]")
        console.print(f"  [red]Failed: {failed}[/red]")

        # Production readiness assessment
        console.print(f"\n[bold]Production Readiness Assessment:[/bold]")

        is_production_ready = failed == 0 and warnings <= 1

        if is_production_ready:
            console.print("[bold green]✓ MarunochiAI is PRODUCTION READY![/bold green]")
            console.print("  All critical tests passed. System is stable and performant.")
        elif failed == 0:
            console.print("[bold yellow]⚠ MarunochiAI is MOSTLY READY[/bold yellow]")
            console.print(f"  Some warnings detected. Review and address before production.")
        else:
            console.print("[bold red]✗ MarunochiAI is NOT READY[/bold red]")
            console.print(f"  {failed} critical failures detected. Must fix before production.")

        # Recommendations
        console.print(f"\n[bold]Recommendations:[/bold]")

        # Latency recommendations
        avg_latencies = [r.avg_latency_ms for r in self.results if r.avg_latency_ms > 0]
        if avg_latencies and statistics.mean(avg_latencies) > 5000:
            console.print("  ⚠️  High average latency detected. Consider:")
            console.print("     - Checking M4 Pro GPU utilization (see M4-PRO-OPTIMIZATION.md)")
            console.print("     - Verifying Ollama Metal acceleration")

        # Error rate recommendations
        error_rates = [r.error_rate for r in self.results]
        if error_rates and max(error_rates) > 0.1:
            console.print("  ⚠️  High error rate detected. Review error logs.")

        # Memory recommendations
        memory_increases = [r.memory_usage_mb for r in self.results if r.memory_usage_mb > 0]
        if memory_increases and max(memory_increases) > 100:
            console.print("  ⚠️  High memory usage detected. Monitor for leaks.")

        return is_production_ready

    async def run_all_tests(self):
        """Run complete stress test suite."""
        console.print(Panel.fit(
            "[bold cyan]MarunochiAI Comprehensive Stress Test Suite[/bold cyan]\n"
            "Testing production readiness...",
            border_style="cyan"
        ))

        # Check server health first
        if not await self.check_server_health():
            return False

        # Start metrics collection in background
        metrics_task = asyncio.create_task(self.collect_system_metrics())

        try:
            # Run all stress tests
            await self.run_concurrent_requests(
                num_requests=50,
                concurrent_limit=10,
                test_name="Light Concurrent Load (50 requests, 10 concurrent)"
            )

            await self.run_concurrent_requests(
                num_requests=100,
                concurrent_limit=20,
                test_name="Heavy Concurrent Load (100 requests, 20 concurrent)"
            )

            await self.test_edge_cases()

            await self.test_a2a_integration_stress()

            await self.test_streaming_stability()

            await self.test_rapid_model_switching()

            await self.test_memory_leak()

        finally:
            # Stop metrics collection
            metrics_task.cancel()
            try:
                await metrics_task
            except asyncio.CancelledError:
                pass

        # Generate and save report
        is_ready = self.generate_final_report()

        # Save detailed results to JSON
        report_path = "/tmp/marunochiAI_stress_test_report.json"
        with open(report_path, "w") as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "production_ready": is_ready,
                "results": [asdict(r) for r in self.results],
                "system_metrics": [asdict(m) for m in self.system_metrics]
            }, f, indent=2)

        console.print(f"\n[dim]Detailed report saved to: {report_path}[/dim]")

        return is_ready


async def main():
    """Main entry point for stress testing."""
    suite = StressTestSuite()

    try:
        is_ready = await suite.run_all_tests()

        if is_ready:
            console.print("\n[bold green]🎉 SUCCESS: MarunochiAI is ready to be the best tool![/bold green]")
            return 0
        else:
            console.print("\n[bold yellow]⚠️  REVIEW NEEDED: Address issues before production use[/bold yellow]")
            return 1
    except KeyboardInterrupt:
        console.print("\n[yellow]Stress test interrupted by user[/yellow]")
        return 2
    except Exception as e:
        console.print(f"\n[red]Fatal error during stress testing:[/red]")
        console.print(traceback.format_exc())
        return 3


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
