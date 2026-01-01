"""
Observability Module

Provides request tracing, metrics collection, and logging utilities
for monitoring cross-agent communication.
"""

import asyncio
import time
import uuid
from collections import defaultdict
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from functools import wraps
from typing import Any, Callable, Dict, List, Optional

import aiohttp
from fastapi import Request, Response
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


# ==================
# Correlation ID
# ==================

# Context variable for correlation ID (thread-safe)
_correlation_id: Optional[str] = None


def generate_correlation_id() -> str:
    """Generate a new correlation ID."""
    return f"maru-{uuid.uuid4().hex[:12]}"


def get_correlation_id() -> Optional[str]:
    """Get current correlation ID."""
    return _correlation_id


def set_correlation_id(correlation_id: str):
    """Set correlation ID for current context."""
    global _correlation_id
    _correlation_id = correlation_id


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """
    Middleware that extracts or generates correlation IDs for request tracing.

    Looks for incoming X-Correlation-ID or X-Request-ID headers,
    or generates a new ID if not present.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        # Extract or generate correlation ID
        correlation_id = (
            request.headers.get("x-correlation-id") or
            request.headers.get("x-request-id") or
            generate_correlation_id()
        )

        # Store in context
        set_correlation_id(correlation_id)

        # Add to request state for access in handlers
        request.state.correlation_id = correlation_id

        # Process request
        response = await call_next(request)

        # Add to response headers
        response.headers["X-Correlation-ID"] = correlation_id

        return response


# ==================
# Metrics Collection
# ==================

@dataclass
class RequestMetrics:
    """Metrics for a single request."""
    path: str
    method: str
    status_code: int
    duration_ms: float
    correlation_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class MetricsCollector:
    """
    Collects and aggregates metrics for monitoring.

    Tracks:
    - Request counts by path/status
    - Request latencies
    - Error rates
    - A2A task metrics
    """

    # Request metrics
    request_count: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    request_latency_sum: Dict[str, float] = field(default_factory=lambda: defaultdict(float))
    request_errors: Dict[str, int] = field(default_factory=lambda: defaultdict(int))

    # A2A metrics
    a2a_tasks_received: int = 0
    a2a_tasks_completed: int = 0
    a2a_tasks_failed: int = 0
    a2a_callback_success: int = 0
    a2a_callback_failed: int = 0

    # BenchAI client metrics
    benchai_requests: int = 0
    benchai_successes: int = 0
    benchai_failures: int = 0
    benchai_circuit_opens: int = 0

    # Recent requests (ring buffer)
    recent_requests: List[RequestMetrics] = field(default_factory=list)
    max_recent: int = 100

    # Start time for uptime calculation
    start_time: datetime = field(default_factory=datetime.utcnow)

    def record_request(self, metrics: RequestMetrics):
        """Record a completed request."""
        key = f"{metrics.method}:{metrics.path}"

        self.request_count[key] += 1
        self.request_latency_sum[key] += metrics.duration_ms

        if metrics.status_code >= 400:
            self.request_errors[key] += 1

        # Add to recent requests (ring buffer)
        self.recent_requests.append(metrics)
        if len(self.recent_requests) > self.max_recent:
            self.recent_requests.pop(0)

    def record_a2a_task(self, status: str):
        """Record A2A task completion."""
        self.a2a_tasks_received += 1
        if status == "completed":
            self.a2a_tasks_completed += 1
        elif status == "failed":
            self.a2a_tasks_failed += 1

    def record_callback(self, success: bool):
        """Record callback execution result."""
        if success:
            self.a2a_callback_success += 1
        else:
            self.a2a_callback_failed += 1

    def record_benchai_request(self, success: bool, circuit_opened: bool = False):
        """Record BenchAI client request."""
        self.benchai_requests += 1
        if success:
            self.benchai_successes += 1
        else:
            self.benchai_failures += 1
        if circuit_opened:
            self.benchai_circuit_opens += 1

    def get_stats(self) -> Dict[str, Any]:
        """Get aggregated metrics."""
        uptime = datetime.utcnow() - self.start_time

        # Calculate average latencies
        avg_latencies = {}
        for key, total in self.request_latency_sum.items():
            count = self.request_count.get(key, 1)
            avg_latencies[key] = round(total / count, 2)

        # Calculate error rate
        total_requests = sum(self.request_count.values())
        total_errors = sum(self.request_errors.values())
        error_rate = (total_errors / total_requests * 100) if total_requests > 0 else 0

        return {
            "uptime_seconds": int(uptime.total_seconds()),
            "uptime_human": str(uptime).split(".")[0],
            "requests": {
                "total": total_requests,
                "by_endpoint": dict(self.request_count),
                "avg_latency_ms": avg_latencies,
                "errors": dict(self.request_errors),
                "error_rate_percent": round(error_rate, 2),
            },
            "a2a": {
                "tasks_received": self.a2a_tasks_received,
                "tasks_completed": self.a2a_tasks_completed,
                "tasks_failed": self.a2a_tasks_failed,
                "success_rate_percent": (
                    round(self.a2a_tasks_completed / self.a2a_tasks_received * 100, 2)
                    if self.a2a_tasks_received > 0 else 100
                ),
                "callbacks_success": self.a2a_callback_success,
                "callbacks_failed": self.a2a_callback_failed,
            },
            "benchai_client": {
                "total_requests": self.benchai_requests,
                "successes": self.benchai_successes,
                "failures": self.benchai_failures,
                "circuit_opens": self.benchai_circuit_opens,
                "success_rate_percent": (
                    round(self.benchai_successes / self.benchai_requests * 100, 2)
                    if self.benchai_requests > 0 else 100
                ),
            },
            "recent_requests": [
                {
                    "path": r.path,
                    "method": r.method,
                    "status": r.status_code,
                    "duration_ms": r.duration_ms,
                    "correlation_id": r.correlation_id,
                    "timestamp": r.timestamp.isoformat(),
                }
                for r in self.recent_requests[-10:]  # Last 10 requests
            ],
        }


# Global metrics collector
_metrics: Optional[MetricsCollector] = None


def get_metrics() -> MetricsCollector:
    """Get or create metrics collector."""
    global _metrics
    if _metrics is None:
        _metrics = MetricsCollector()
    return _metrics


def reset_metrics():
    """Reset metrics (for testing)."""
    global _metrics
    _metrics = MetricsCollector()


# ==================
# Logging Middleware
# ==================

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that logs requests with timing and correlation IDs.
    """

    # Paths to exclude from logging (health checks, etc.)
    EXCLUDE_PATHS = {"/health", "/favicon.ico"}

    async def dispatch(self, request: Request, call_next) -> Response:
        # Skip excluded paths
        if request.url.path in self.EXCLUDE_PATHS:
            return await call_next(request)

        start_time = time.time()
        correlation_id = getattr(request.state, "correlation_id", "unknown")

        # Log request
        logger.info(
            f"[{correlation_id}] --> {request.method} {request.url.path}"
        )

        # Process request
        response = await call_next(request)

        # Calculate duration
        duration_ms = (time.time() - start_time) * 1000

        # Record metrics
        metrics = get_metrics()
        metrics.record_request(RequestMetrics(
            path=request.url.path,
            method=request.method,
            status_code=response.status_code,
            duration_ms=duration_ms,
            correlation_id=correlation_id,
        ))

        # Log response
        log_level = "warning" if response.status_code >= 400 else "info"
        getattr(logger, log_level)(
            f"[{correlation_id}] <-- {response.status_code} "
            f"({duration_ms:.1f}ms)"
        )

        return response


# ==================
# Callback Execution
# ==================

async def execute_callback(
    callback_url: str,
    result: Dict[str, Any],
    correlation_id: Optional[str] = None,
    timeout: float = 10.0
) -> bool:
    """
    Execute A2A callback to notify task completion.

    Args:
        callback_url: URL to POST result to
        result: Task result data
        correlation_id: Correlation ID for tracing
        timeout: Request timeout in seconds

    Returns:
        True if callback succeeded, False otherwise
    """
    metrics = get_metrics()
    correlation_id = correlation_id or get_correlation_id() or generate_correlation_id()

    headers = {
        "Content-Type": "application/json",
        "X-Correlation-ID": correlation_id,
        "X-Callback-Source": "marunochiAI",
    }

    try:
        logger.info(f"[{correlation_id}] Executing callback to {callback_url}")

        async with aiohttp.ClientSession() as session:
            async with session.post(
                callback_url,
                json=result,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=timeout)
            ) as response:
                if response.status in (200, 201, 202, 204):
                    logger.info(
                        f"[{correlation_id}] Callback succeeded: {response.status}"
                    )
                    metrics.record_callback(success=True)
                    return True
                else:
                    logger.warning(
                        f"[{correlation_id}] Callback failed: HTTP {response.status}"
                    )
                    metrics.record_callback(success=False)
                    return False

    except aiohttp.ClientError as e:
        logger.warning(f"[{correlation_id}] Callback connection error: {e}")
        metrics.record_callback(success=False)
        return False

    except asyncio.TimeoutError:
        logger.warning(f"[{correlation_id}] Callback timed out after {timeout}s")
        metrics.record_callback(success=False)
        return False

    except Exception as e:
        logger.error(f"[{correlation_id}] Callback unexpected error: {e}")
        metrics.record_callback(success=False)
        return False


# ==================
# Tracing Decorator
# ==================

def traced(name: Optional[str] = None):
    """
    Decorator that adds tracing to async functions.

    Logs entry/exit with timing and correlation ID.

    Args:
        name: Optional span name (defaults to function name)
    """
    def decorator(func: Callable) -> Callable:
        span_name = name or func.__name__

        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            correlation_id = get_correlation_id() or "no-trace"
            start_time = time.time()

            logger.debug(f"[{correlation_id}] ENTER {span_name}")

            try:
                result = await func(*args, **kwargs)
                duration_ms = (time.time() - start_time) * 1000
                logger.debug(
                    f"[{correlation_id}] EXIT {span_name} ({duration_ms:.1f}ms)"
                )
                return result

            except Exception as e:
                duration_ms = (time.time() - start_time) * 1000
                logger.warning(
                    f"[{correlation_id}] ERROR {span_name}: {e} ({duration_ms:.1f}ms)"
                )
                raise

        return wrapper
    return decorator


# ==================
# Header Propagation
# ==================

def get_trace_headers() -> Dict[str, str]:
    """
    Get headers for propagating trace context to downstream services.

    Returns headers suitable for cross-agent communication.
    """
    correlation_id = get_correlation_id()

    headers = {
        "X-Correlation-ID": correlation_id or generate_correlation_id(),
        "X-Source-Agent": "marunochiAI",
        "X-Timestamp": datetime.utcnow().isoformat(),
    }

    return headers
