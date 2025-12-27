"""FastAPI server with OpenAI-compatible endpoints."""

import time
import uuid
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from loguru import logger

from ..core.inference import InferenceEngine, ModelSize
from .models import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionChoice,
    Usage,
    ChatMessage,
    HealthResponse,
)


# Global inference engine
engine: InferenceEngine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize and cleanup resources."""
    global engine

    logger.info("Starting MarunochiAI server...")

    # Initialize inference engine
    engine = InferenceEngine(
        ollama_host="http://localhost:11434",
        enable_custom=True  # Use fine-tuned model if available
    )

    # Health check
    healthy = await engine.health_check()
    if not healthy:
        logger.warning("Ollama health check failed, but continuing anyway")

    logger.info("MarunochiAI server ready")

    yield

    logger.info("Shutting down MarunochiAI server...")


# Create FastAPI app
app = FastAPI(
    title="MarunochiAI",
    description="The most powerful self-hosted coding assistant",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    try:
        healthy = await engine.health_check()

        return HealthResponse(
            status="healthy" if healthy else "degraded",
            ollama_available=healthy,
            models_loaded=[
                ModelSize.FAST,
                ModelSize.POWERFUL,
            ],
            version="0.1.0",
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return HealthResponse(
            status="unhealthy",
            ollama_available=False,
            models_loaded=[],
            version="0.1.0",
        )


@app.post("/v1/chat/completions")
async def chat_completions(
    request: ChatCompletionRequest
) -> ChatCompletionResponse | StreamingResponse:
    """
    OpenAI-compatible chat completions endpoint.

    Supports both streaming and non-streaming responses.
    """
    try:
        # Convert messages to Ollama format
        messages = [
            {"role": msg.role, "content": msg.content}
            for msg in request.messages
        ]

        # Parse model (allow override)
        model = None
        if request.model and request.model in [m.value for m in ModelSize]:
            model = ModelSize(request.model)

        if request.stream:
            # Streaming response
            return StreamingResponse(
                _stream_completion(messages, model, request),
                media_type="text/event-stream"
            )
        else:
            # Non-streaming response
            content = await engine.chat(
                messages=messages,
                model=model,
                stream=False,
                options={
                    "temperature": request.temperature,
                    "top_p": request.top_p,
                    "num_predict": request.max_tokens,
                }
            )

            # Build OpenAI-compatible response
            response = ChatCompletionResponse(
                id=f"chatcmpl-{uuid.uuid4().hex[:8]}",
                created=int(time.time()),
                model=model.value if model else "auto",
                choices=[
                    ChatCompletionChoice(
                        index=0,
                        message=ChatMessage(role="assistant", content=content),
                        finish_reason="stop",
                    )
                ],
                usage=Usage(
                    prompt_tokens=sum(len(m["content"].split()) for m in messages),
                    completion_tokens=len(content.split()),
                    total_tokens=sum(len(m["content"].split()) for m in messages) + len(content.split()),
                ),
            )

            return response

    except Exception as e:
        logger.error(f"Chat completion failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


async def _stream_completion(
    messages: list,
    model: ModelSize,
    request: ChatCompletionRequest
) -> AsyncIterator[str]:
    """
    Stream chat completion in SSE format.

    Args:
        messages: Chat messages
        model: Selected model
        request: Original request

    Yields:
        SSE-formatted chunks
    """
    try:
        chunk_id = f"chatcmpl-{uuid.uuid4().hex[:8]}"

        async for token in await engine.chat(
            messages=messages,
            model=model,
            stream=True,
            options={
                "temperature": request.temperature,
                "top_p": request.top_p,
                "num_predict": request.max_tokens,
            }
        ):
            # Format as SSE
            chunk_data = {
                "id": chunk_id,
                "object": "chat.completion.chunk",
                "created": int(time.time()),
                "model": model.value if model else "auto",
                "choices": [
                    {
                        "index": 0,
                        "delta": {"content": token},
                        "finish_reason": None,
                    }
                ],
            }

            yield f"data: {chunk_data}\n\n"

        # Send final chunk
        final_chunk = {
            "id": chunk_id,
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model.value if model else "auto",
            "choices": [
                {
                    "index": 0,
                    "delta": {},
                    "finish_reason": "stop",
                }
            ],
        }
        yield f"data: {final_chunk}\n\n"
        yield "data: [DONE]\n\n"

    except Exception as e:
        logger.error(f"Streaming failed: {e}")
        error_chunk = {"error": str(e)}
        yield f"data: {error_chunk}\n\n"


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "MarunochiAI",
        "version": "0.1.0",
        "description": "The most powerful self-hosted coding assistant",
        "endpoints": {
            "health": "/health",
            "chat": "/v1/chat/completions",
        },
    }


def start():
    """Start the server (for CLI entrypoint)."""
    import uvicorn

    uvicorn.run(
        "marunochithe.api.server:app",
        host="0.0.0.0",
        port=8765,
        reload=True,
        log_level="info",
    )


if __name__ == "__main__":
    start()
