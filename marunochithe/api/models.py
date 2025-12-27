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


# A2A Integration Models (for BenchAI integration)

class SyncRequest(BaseModel):
    """Request to sync data from another agent."""
    from_agent: str
    sync_type: str  # "experience", "knowledge", "pattern"
    items: List[Dict]
    timestamp: Optional[str] = None


class SyncResponse(BaseModel):
    """Response to sync request."""
    status: str
    from_agent: str
    items_processed: int
    sync_type: str


class ShareRequest(BaseModel):
    """Request to share data with another agent."""
    requester: str
    sync_type: str = "experience"
    since: Optional[str] = None
    limit: int = 50


class ShareResponse(BaseModel):
    """Response containing shared data."""
    status: str
    for_agent: str
    sync_type: str
    items: List[Dict]
    count: int


class A2ATaskRequest(BaseModel):
    """Task request from another agent."""
    from_agent: str
    task_type: str
    task_description: str
    context: Optional[Dict] = None
    priority: str = "normal"
    callback_url: Optional[str] = None


class A2ATaskResponse(BaseModel):
    """Response to task request."""
    task_id: str
    status: str  # "completed", "pending", "failed"
    result: Optional[Dict] = None
    message: Optional[str] = None
