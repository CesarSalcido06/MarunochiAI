"""
MarunochiAI Configuration Module

Centralized configuration management using environment variables.
Loads .env file and provides validated settings via Pydantic.
"""

import os
from pathlib import Path
from typing import Optional
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


def find_env_file() -> Optional[Path]:
    """Find .env file, checking multiple locations."""
    # Check in order: CWD, project root, home directory
    locations = [
        Path.cwd() / ".env",
        Path(__file__).parent.parent / ".env",  # Project root
        Path.home() / "MarunochiAI" / ".env",
    ]

    for loc in locations:
        if loc.exists():
            return loc
    return None


class OllamaSettings(BaseSettings):
    """Ollama server configuration."""

    host: str = Field(
        default="http://localhost:11434",
        alias="OLLAMA_HOST",
        description="Ollama server URL"
    )
    max_loaded_models: int = Field(
        default=2,
        alias="OLLAMA_MAX_LOADED_MODELS"
    )
    keep_alive: str = Field(
        default="30m",
        alias="OLLAMA_KEEP_ALIVE"
    )


class BenchAISettings(BaseSettings):
    """BenchAI integration configuration."""

    url: str = Field(
        default="http://localhost:8085",
        alias="BENCHAI_URL",
        description="BenchAI orchestrator URL"
    )
    api_key: Optional[str] = Field(
        default=None,
        alias="BENCHAI_API_KEY",
        description="Optional API key for BenchAI"
    )
    agent_id: str = Field(
        default="marunochiAI",
        alias="BENCHAI_AGENT_ID",
        description="Agent identifier for A2A protocol"
    )
    heartbeat_interval: int = Field(
        default=30,
        alias="BENCHAI_HEARTBEAT_INTERVAL",
        description="Heartbeat interval in seconds"
    )


class ServerSettings(BaseSettings):
    """MarunochiAI server configuration."""

    host: str = Field(
        default="0.0.0.0",
        alias="MARUNOCHITHE_HOST"
    )
    port: int = Field(
        default=8765,
        alias="MARUNOCHITHE_PORT"
    )
    log_level: str = Field(
        default="INFO",
        alias="MARUNOCHITHE_LOG_LEVEL"
    )
    log_file: Optional[str] = Field(
        default=None,
        alias="MARUNOCHITHE_LOG_FILE"
    )
    default_model: str = Field(
        default="qwen2.5-coder:7b",
        alias="MARUNOCHITHE_DEFAULT_MODEL"
    )
    enable_custom: bool = Field(
        default=True,
        alias="MARUNOCHITHE_ENABLE_CUSTOM"
    )


class ChromaSettings(BaseSettings):
    """ChromaDB configuration."""

    path: str = Field(
        default="~/MarunochiAI/data/chroma",
        alias="CHROMA_PATH"
    )
    collection_name: str = Field(
        default="codebase",
        alias="CHROMA_COLLECTION_NAME"
    )

    @property
    def resolved_path(self) -> Path:
        """Return expanded path."""
        return Path(self.path).expanduser()


class Settings(BaseSettings):
    """Main configuration container."""

    # Nested settings
    ollama: OllamaSettings = Field(default_factory=OllamaSettings)
    benchai: BenchAISettings = Field(default_factory=BenchAISettings)
    server: ServerSettings = Field(default_factory=ServerSettings)
    chroma: ChromaSettings = Field(default_factory=ChromaSettings)

    # Development flags
    debug: bool = Field(default=False, alias="DEBUG")
    reload: bool = Field(default=False, alias="RELOAD")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


# Global settings instance
_settings: Optional[Settings] = None


def load_settings(env_file: Optional[Path] = None) -> Settings:
    """
    Load settings from environment and .env file.

    Args:
        env_file: Optional path to .env file. If not provided,
                  searches common locations.

    Returns:
        Settings instance
    """
    global _settings

    # Find .env file if not specified
    if env_file is None:
        env_file = find_env_file()

    # Load .env file if found
    if env_file and env_file.exists():
        from dotenv import load_dotenv
        load_dotenv(env_file)
        print(f"[CONFIG] Loaded environment from {env_file}")

    # Create settings (reads from environment)
    _settings = Settings()

    return _settings


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Returns:
        Settings instance (cached after first call)
    """
    global _settings
    if _settings is None:
        _settings = load_settings()
    return _settings


def refresh_settings() -> Settings:
    """
    Reload settings from environment.

    Clears cache and reloads from .env file.

    Returns:
        Fresh Settings instance
    """
    global _settings
    get_settings.cache_clear()
    _settings = None
    return load_settings()


# Convenience accessors
def get_ollama_host() -> str:
    """Get Ollama server URL."""
    return get_settings().ollama.host


def get_benchai_url() -> str:
    """Get BenchAI orchestrator URL."""
    return get_settings().benchai.url


def get_agent_id() -> str:
    """Get agent identifier for A2A protocol."""
    return get_settings().benchai.agent_id
