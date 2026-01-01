"""Client for reporting to BenchAI collective learning system."""

import asyncio
import aiohttp
from typing import Dict, Any, Optional
from loguru import logger

from ..config import get_settings, get_benchai_url, get_agent_id
from ..resilience import (
    get_circuit,
    CircuitOpenError,
    with_retry,
    check_connectivity,
)


class BenchAIClient:
    """
    Client for interacting with BenchAI's collective learning endpoints.

    This allows MarunochiAI to report task completions, share experiences,
    and participate in the multi-agent learning ecosystem.

    Configuration is loaded from environment variables via config module.
    """

    def __init__(self, benchai_url: Optional[str] = None, agent_id: Optional[str] = None):
        """
        Initialize BenchAI client.

        Args:
            benchai_url: Base URL for BenchAI server. If not provided,
                        reads from BENCHAI_URL environment variable.
            agent_id: Agent identifier. If not provided,
                     reads from BENCHAI_AGENT_ID environment variable.
        """
        self.base_url = benchai_url or get_benchai_url()
        self.agent_id = agent_id or get_agent_id()

        # Circuit breaker for this BenchAI connection
        self._circuit = get_circuit(
            name="benchai",
            failure_threshold=5,
            recovery_timeout=30.0,
            half_open_max_calls=1
        )

        logger.info(
            f"[BenchAI Client] Initialized with URL={self.base_url}, "
            f"agent_id={self.agent_id}"
        )

    def get_circuit_status(self) -> dict:
        """Get current circuit breaker status."""
        return self._circuit.get_status()

    async def report_task_completion(
        self,
        task_type: str,
        success: bool,
        metrics: Dict[str, Any],
        description: Optional[str] = None
    ) -> bool:
        """
        Report task completion to BenchAI for learning.

        Args:
            task_type: Type of task (e.g., "code_search", "refactoring")
            success: Whether the task succeeded
            metrics: Task-specific metrics (e.g., duration_ms, files_modified)
            description: Optional description of what was done

        Returns:
            True if report was successful, False otherwise
        """
        # Check circuit breaker first
        if not self._circuit.can_execute():
            logger.warning(
                f"[BenchAI] Circuit OPEN - skipping report for {task_type}"
            )
            return False

        try:
            result = await self._report_task_with_retry(
                task_type, success, metrics, description
            )
            self._circuit.record_success()
            return result
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            self._circuit.record_failure()
            logger.warning(f"[BenchAI] Report failed (circuit: {self._circuit.state.value}): {e}")
            return False
        except Exception as e:
            self._circuit.record_failure()
            logger.error(f"[BenchAI] Unexpected error: {e}")
            return False

    @with_retry(max_attempts=3, min_wait=0.5, max_wait=5.0)
    async def _report_task_with_retry(
        self,
        task_type: str,
        success: bool,
        metrics: Dict[str, Any],
        description: Optional[str]
    ) -> bool:
        """Internal method with retry logic."""
        async with aiohttp.ClientSession() as session:
            payload = {
                "agent_id": self.agent_id,
                "contribution_type": "experience",
                "content": description or f"Task: {task_type}, Success: {success}",
                "domain": "coding",
                "quality_score": 0.9 if success else 0.3,
                "metadata": {
                    "task_type": task_type,
                    "success": success,
                    **metrics
                }
            }

            async with session.post(
                f"{self.base_url}/v1/learning/collective/contribute",
                json=payload,
                timeout=aiohttp.ClientTimeout(total=5)
            ) as response:
                if response.status == 200:
                    logger.info(
                        f"Reported task completion to BenchAI: "
                        f"{task_type} (success={success})"
                    )
                    return True
                else:
                    logger.warning(
                        f"Failed to report to BenchAI: "
                        f"HTTP {response.status}"
                    )
                    return False

    async def sync_with_benchai(
        self,
        sync_type: str = "experience",
        limit: int = 50
    ) -> Optional[Dict]:
        """
        Pull experiences/knowledge from BenchAI.

        Args:
            sync_type: Type of data to sync ("experience", "knowledge", "pattern")
            limit: Maximum number of items to pull

        Returns:
            Dict with sync data or None if failed
        """
        if not self._circuit.can_execute():
            logger.warning(f"[BenchAI] Circuit OPEN - skipping sync pull")
            return None

        try:
            result = await self._sync_with_retry(sync_type, limit)
            self._circuit.record_success()
            return result
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            self._circuit.record_failure()
            logger.warning(f"[BenchAI] Sync failed (circuit: {self._circuit.state.value}): {e}")
            return None
        except Exception as e:
            self._circuit.record_failure()
            logger.error(f"[BenchAI] Unexpected sync error: {e}")
            return None

    @with_retry(max_attempts=3, min_wait=0.5, max_wait=5.0)
    async def _sync_with_retry(self, sync_type: str, limit: int) -> Optional[Dict]:
        """Internal sync with retry logic."""
        async with aiohttp.ClientSession() as session:
            params = {
                "requester": self.agent_id,
                "sync_type": sync_type,
                "limit": limit
            }

            async with session.get(
                f"{self.base_url}/v1/learning/sync/share",
                params=params,
                timeout=aiohttp.ClientTimeout(total=5)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(
                        f"Synced {data.get('count', 0)} {sync_type} items "
                        f"from BenchAI"
                    )
                    return data
                else:
                    logger.warning(
                        f"Failed to sync with BenchAI: "
                        f"HTTP {response.status}"
                    )
                    return None

    async def push_to_benchai(
        self,
        sync_type: str,
        items: list
    ) -> bool:
        """
        Push experiences/knowledge to BenchAI.

        Args:
            sync_type: Type of data to push ("experience", "knowledge", "pattern")
            items: List of items to push

        Returns:
            True if successful, False otherwise
        """
        if not self._circuit.can_execute():
            logger.warning(f"[BenchAI] Circuit OPEN - skipping push")
            return False

        try:
            result = await self._push_with_retry(sync_type, items)
            self._circuit.record_success()
            return result
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            self._circuit.record_failure()
            logger.warning(f"[BenchAI] Push failed (circuit: {self._circuit.state.value}): {e}")
            return False
        except Exception as e:
            self._circuit.record_failure()
            logger.error(f"[BenchAI] Unexpected push error: {e}")
            return False

    @with_retry(max_attempts=3, min_wait=0.5, max_wait=5.0)
    async def _push_with_retry(self, sync_type: str, items: list) -> bool:
        """Internal push with retry logic."""
        async with aiohttp.ClientSession() as session:
            payload = {
                "from_agent": self.agent_id,
                "sync_type": sync_type,
                "items": items
            }

            async with session.post(
                f"{self.base_url}/v1/learning/sync/receive",
                json=payload,
                timeout=aiohttp.ClientTimeout(total=5)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(
                        f"Pushed {data.get('items_processed', 0)} {sync_type} "
                        f"items to BenchAI"
                    )
                    return True
                else:
                    logger.warning(
                        f"Failed to push to BenchAI: "
                        f"HTTP {response.status}"
                    )
                    return False

    async def health_check(self) -> bool:
        """
        Check if BenchAI is available.

        Note: Health checks bypass the circuit breaker to allow
        recovery detection even when circuit is open.

        Returns:
            True if BenchAI is reachable, False otherwise
        """
        healthy, error = await check_connectivity(
            f"{self.base_url}/health",
            timeout=3.0,
            expected_status=200
        )

        if healthy:
            logger.debug(f"BenchAI health check passed: {self.base_url}")
        else:
            logger.warning(f"BenchAI health check failed: {error}")

        return healthy
