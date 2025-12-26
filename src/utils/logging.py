"""Logging configuration for MarunochiAI."""

import sys
from pathlib import Path
from loguru import logger


def setup_logging(
    log_level: str = "INFO",
    log_file: str = None,
    rotation: str = "100 MB",
    retention: str = "1 week",
):
    """
    Configure logging for MarunochiAI.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Path to log file (optional)
        rotation: Log rotation size
        retention: Log retention period
    """
    # Remove default handler
    logger.remove()

    # Console handler with colors
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=log_level,
        colorize=True,
    )

    # File handler (if specified)
    if log_file:
        log_path = Path(log_file).expanduser()
        log_path.parent.mkdir(parents=True, exist_ok=True)

        logger.add(
            str(log_path),
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            level=log_level,
            rotation=rotation,
            retention=retention,
            compression="zip",
        )

        logger.info(f"Logging to file: {log_path}")

    logger.info(f"Logging initialized at {log_level} level")


# Auto-setup on import
setup_logging(
    log_level="INFO",
    log_file="~/MarunochiAI/data/logs/marunochithe.log"
)
