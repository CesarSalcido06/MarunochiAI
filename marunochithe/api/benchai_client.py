"""Client for reporting to BenchAI collective learning system."""

import aiohttp
from typing import Dict, Any, Optional
from loguru import logger


class BenchAIClient:
    """
    Client for interacting with BenchAI's collective learning endpoints.

    This allows MarunochiAI to report task completions, share experiences,
    and participate in the multi-agent learning ecosystem.
    """

    def __init__(self, benchai_url: str = "http://localhost:8085"):
        """
        Initialize BenchAI client.

        Args:
            benchai_url: Base URL for BenchAI server
        """
        self.base_url = benchai_url
        self.agent_id = "marunochiAI"

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
        try:
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

        except aiohttp.ClientError as e:
            logger.debug(f"Could not connect to BenchAI: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error reporting to BenchAI: {e}")
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
        try:
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

        except aiohttp.ClientError as e:
            logger.debug(f"Could not connect to BenchAI: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error syncing with BenchAI: {e}")
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
        try:
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

        except aiohttp.ClientError as e:
            logger.debug(f"Could not connect to BenchAI: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error pushing to BenchAI: {e}")
            return False

    async def health_check(self) -> bool:
        """
        Check if BenchAI is available.

        Returns:
            True if BenchAI is reachable, False otherwise
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self.base_url}/health",
                    timeout=aiohttp.ClientTimeout(total=2)
                ) as response:
                    return response.status == 200

        except Exception:
            return False
