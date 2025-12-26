"""Pydantic models for API requests and responses."""

from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """Chat message in OpenAI format."""
    role: Literal["system", "user", "assistant"]
    content: str


class ChatCompletionRequest(BaseModel):
    """Chat completion request (OpenAI-compatible)."""
    model: Optional[str] = "qwen2.5-coder:7b"
    messages: List[ChatMessage]
    temperature: Optional[float] = Field(default=0.1, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(default=2048, ge=1, le=32768)
    stream: Optional[bool] = False
    top_p: Optional[float] = Field(default=0.95, ge=0.0, le=1.0)


class ChatCompletionChoice(BaseModel):
    """Chat completion choice."""
    index: int
    message: ChatMessage
    finish_reason: Literal["stop", "length", "error"]


class Usage(BaseModel):
    """Token usage statistics."""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    """Chat completion response (OpenAI-compatible)."""
    id: str
    object: Literal["chat.completion"] = "chat.completion"
    created: int
    model: str
    choices: List[ChatCompletionChoice]
    usage: Usage


class CodebaseSearchRequest(BaseModel):
    """Codebase semantic search request."""
    query: str
    limit: Optional[int] = Field(default=5, ge=1, le=50)
    file_types: Optional[List[str]] = None  # e.g., [".py", ".js"]


class CodebaseSearchResult(BaseModel):
    """Single search result."""
    filepath: str
    content: str
    similarity: float
    metadata: Dict


class CodebaseSearchResponse(BaseModel):
    """Codebase search response."""
    query: str
    results: List[CodebaseSearchResult]
    total: int


class HealthResponse(BaseModel):
    """Health check response."""
    status: Literal["healthy", "degraded", "unhealthy"]
    ollama_available: bool
    models_loaded: List[str]
    version: str
