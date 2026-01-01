"""
Network Resilience Module

Provides retry logic, circuit breaker, and fault tolerance patterns
for cross-agent communication.
"""

import asyncio
import time
from dataclasses import dataclass, field
from enum import Enum
from functools import wraps
from typing import Any, Callable, Optional, Type, Union

import aiohttp
from loguru import logger
from tenacity import (
    AsyncRetrying,
    RetryError,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log,
)


# ==================
# Circuit Breaker
# ==================

class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject calls
    HALF_OPEN = "half_open"  # Testing if recovered


@dataclass
class CircuitBreaker:
    """
    Circuit breaker pattern for preventing cascade failures.

    When too many failures occur, the circuit "opens" and rejects
    calls immediately. After a timeout, it enters "half-open" state
    to test if the service has recovered.

    Attributes:
        name: Identifier for this circuit
        failure_threshold: Number of failures before opening
        recovery_timeout: Seconds to wait before testing recovery
        half_open_max_calls: Max calls allowed in half-open state
    """
    name: str
    failure_threshold: int = 5
    recovery_timeout: float = 30.0
    half_open_max_calls: int = 1

    # Internal state
    _state: CircuitState = field(default=CircuitState.CLOSED, init=False)
    _failure_count: int = field(default=0, init=False)
    _last_failure_time: float = field(default=0.0, init=False)
    _half_open_calls: int = field(default=0, init=False)

    @property
    def state(self) -> CircuitState:
        """Get current circuit state, checking for recovery."""
        if self._state == CircuitState.OPEN:
            # Check if recovery timeout has passed
            if time.time() - self._last_failure_time >= self.recovery_timeout:
                self._state = CircuitState.HALF_OPEN
                self._half_open_calls = 0
                logger.info(f"[Circuit:{self.name}] Transitioning to HALF_OPEN")
        return self._state

    def record_success(self):
        """Record a successful call."""
        if self._state == CircuitState.HALF_OPEN:
            self._state = CircuitState.CLOSED
            self._failure_count = 0
            logger.info(f"[Circuit:{self.name}] Recovered, now CLOSED")
        elif self._state == CircuitState.CLOSED:
            # Reset failure count on success
            self._failure_count = 0

    def record_failure(self):
        """Record a failed call."""
        self._failure_count += 1
        self._last_failure_time = time.time()

        if self._state == CircuitState.HALF_OPEN:
            # Failure during recovery test
            self._state = CircuitState.OPEN
            logger.warning(f"[Circuit:{self.name}] Recovery failed, back to OPEN")

        elif self._state == CircuitState.CLOSED:
            if self._failure_count >= self.failure_threshold:
                self._state = CircuitState.OPEN
                logger.warning(
                    f"[Circuit:{self.name}] Threshold reached ({self._failure_count}), "
                    f"now OPEN for {self.recovery_timeout}s"
                )

    def can_execute(self) -> bool:
        """Check if a call is allowed."""
        state = self.state  # This may transition OPEN -> HALF_OPEN

        if state == CircuitState.CLOSED:
            return True

        if state == CircuitState.OPEN:
            return False

        if state == CircuitState.HALF_OPEN:
            if self._half_open_calls < self.half_open_max_calls:
                self._half_open_calls += 1
                return True
            return False

        return False

    def get_status(self) -> dict:
        """Get circuit status for monitoring."""
        return {
            "name": self.name,
            "state": self.state.value,
            "failure_count": self._failure_count,
            "failure_threshold": self.failure_threshold,
            "recovery_timeout": self.recovery_timeout,
            "time_since_last_failure": (
                time.time() - self._last_failure_time
                if self._last_failure_time > 0 else None
            )
        }


class CircuitOpenError(Exception):
    """Raised when circuit is open and call is rejected."""
    pass


# Global circuit breakers registry
_circuits: dict[str, CircuitBreaker] = {}


def get_circuit(name: str, **kwargs) -> CircuitBreaker:
    """Get or create a circuit breaker by name."""
    if name not in _circuits:
        _circuits[name] = CircuitBreaker(name=name, **kwargs)
    return _circuits[name]


def get_all_circuits() -> dict[str, dict]:
    """Get status of all circuit breakers."""
    return {name: cb.get_status() for name, cb in _circuits.items()}


# ==================
# Retry Decorators
# ==================

def with_retry(
    max_attempts: int = 3,
    min_wait: float = 1.0,
    max_wait: float = 10.0,
    retry_on: tuple = (aiohttp.ClientError, asyncio.TimeoutError),
):
    """
    Decorator for async functions with exponential backoff retry.

    Args:
        max_attempts: Maximum retry attempts
        min_wait: Minimum wait between retries (seconds)
        max_wait: Maximum wait between retries (seconds)
        retry_on: Exception types to retry on
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            attempt = 0
            last_exception = None

            async for attempt_info in AsyncRetrying(
                stop=stop_after_attempt(max_attempts),
                wait=wait_exponential(multiplier=1, min=min_wait, max=max_wait),
                retry=retry_if_exception_type(retry_on),
                reraise=True,
            ):
                with attempt_info:
                    attempt += 1
                    if attempt > 1:
                        logger.debug(
                            f"[Retry] {func.__name__} attempt {attempt}/{max_attempts}"
                        )
                    return await func(*args, **kwargs)

        return wrapper
    return decorator


def with_circuit_breaker(circuit_name: str, **circuit_kwargs):
    """
    Decorator that wraps a function with circuit breaker protection.

    Args:
        circuit_name: Name for the circuit breaker
        **circuit_kwargs: Additional args for CircuitBreaker
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            circuit = get_circuit(circuit_name, **circuit_kwargs)

            if not circuit.can_execute():
                logger.warning(
                    f"[Circuit:{circuit_name}] OPEN - rejecting call to {func.__name__}"
                )
                raise CircuitOpenError(
                    f"Circuit {circuit_name} is open, call rejected"
                )

            try:
                result = await func(*args, **kwargs)
                circuit.record_success()
                return result
            except Exception as e:
                circuit.record_failure()
                raise

        return wrapper
    return decorator


def resilient(
    circuit_name: str,
    max_attempts: int = 3,
    min_wait: float = 1.0,
    max_wait: float = 10.0,
    failure_threshold: int = 5,
    recovery_timeout: float = 30.0,
):
    """
    Combined decorator with both retry and circuit breaker.

    Retries happen within the circuit breaker, so failed retries
    count as a single failure for the circuit.

    Args:
        circuit_name: Name for the circuit breaker
        max_attempts: Maximum retry attempts
        min_wait: Minimum wait between retries
        max_wait: Maximum wait between retries
        failure_threshold: Failures before circuit opens
        recovery_timeout: Seconds before testing recovery
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            circuit = get_circuit(
                circuit_name,
                failure_threshold=failure_threshold,
                recovery_timeout=recovery_timeout
            )

            if not circuit.can_execute():
                logger.warning(
                    f"[Circuit:{circuit_name}] OPEN - rejecting {func.__name__}"
                )
                raise CircuitOpenError(f"Circuit {circuit_name} is open")

            try:
                # Retry logic
                async for attempt_info in AsyncRetrying(
                    stop=stop_after_attempt(max_attempts),
                    wait=wait_exponential(multiplier=1, min=min_wait, max=max_wait),
                    retry=retry_if_exception_type(
                        (aiohttp.ClientError, asyncio.TimeoutError)
                    ),
                    reraise=True,
                ):
                    with attempt_info:
                        result = await func(*args, **kwargs)
                        circuit.record_success()
                        return result

            except Exception as e:
                circuit.record_failure()
                raise

        return wrapper
    return decorator


# ==================
# Health Check Utils
# ==================

async def check_connectivity(
    url: str,
    timeout: float = 5.0,
    expected_status: int = 200
) -> tuple[bool, Optional[str]]:
    """
    Check if a URL is reachable.

    Args:
        url: URL to check
        timeout: Request timeout in seconds
        expected_status: Expected HTTP status code

    Returns:
        Tuple of (is_healthy, error_message)
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url,
                timeout=aiohttp.ClientTimeout(total=timeout)
            ) as response:
                if response.status == expected_status:
                    return (True, None)
                else:
                    return (False, f"Unexpected status: {response.status}")

    except aiohttp.ClientError as e:
        return (False, f"Connection error: {e}")
    except asyncio.TimeoutError:
        return (False, f"Timeout after {timeout}s")
    except Exception as e:
        return (False, f"Unexpected error: {e}")


async def validate_connectivity_at_startup(
    services: dict[str, str],
    required: list[str] = None,
    timeout: float = 5.0
) -> dict[str, dict]:
    """
    Validate connectivity to multiple services at startup.

    Args:
        services: Dict of service_name -> health_url
        required: List of services that must be reachable (raises if not)
        timeout: Per-service timeout

    Returns:
        Dict of service_name -> {healthy: bool, error: str|None}

    Raises:
        ConnectionError: If a required service is unreachable
    """
    required = required or []
    results = {}

    for name, url in services.items():
        healthy, error = await check_connectivity(url, timeout)
        results[name] = {"healthy": healthy, "error": error, "url": url}

        if healthy:
            logger.info(f"[Startup] {name} is reachable at {url}")
        else:
            if name in required:
                logger.error(f"[Startup] REQUIRED service {name} is unreachable: {error}")
                raise ConnectionError(
                    f"Required service {name} at {url} is unreachable: {error}"
                )
            else:
                logger.warning(f"[Startup] Optional service {name} is unreachable: {error}")

    return results
