"""FastAPI server with OpenAI-compatible endpoints."""

import json
import time
import uuid
from contextlib import asynccontextmanager
from typing import AsyncIterator, Union, Dict, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from loguru import logger

from ..config import load_settings, get_settings
from ..core.inference import InferenceEngine, ModelSize
from ..code_understanding import (
    CodeParser,
    CodeChunker,
    CodebaseIndexer,
    KeywordIndexer,
    HybridSearcher,
    CodebaseWatcher,
)
from .benchai_client import BenchAIClient
from .models import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionChoice,
    Usage,
    ChatMessage,
    HealthResponse,
    CodebaseSearchRequest,
    CodebaseSearchResponse,
    CodebaseSearchResult,
    SyncRequest,
    SyncResponse,
    ShareRequest,
    ShareResponse,
    A2ATaskRequest,
    A2ATaskResponse,
)


# Global inference engine
engine: InferenceEngine = None

# Global code understanding components
code_indexer: CodebaseIndexer = None
hybrid_searcher: HybridSearcher = None
code_watcher: CodebaseWatcher = None

# Global BenchAI client for multi-agent integration
benchai_client: BenchAIClient = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize and cleanup resources."""
    global engine, code_indexer, hybrid_searcher, code_watcher, benchai_client

    logger.info("Starting MarunochiAI server...")

    # Load configuration from .env file
    settings = load_settings()
    logger.info(f"[CONFIG] Ollama: {settings.ollama.host}")
    logger.info(f"[CONFIG] BenchAI: {settings.benchai.url}")
    logger.info(f"[CONFIG] Agent ID: {settings.benchai.agent_id}")

    # Initialize inference engine with configured Ollama host
    engine = InferenceEngine(
        ollama_host=settings.ollama.host,
        enable_custom=settings.server.enable_custom
    )

    # Health check
    healthy = await engine.health_check()
    if not healthy:
        logger.warning("Ollama health check failed, but continuing anyway")

    # Initialize code understanding components (optional)
    try:
        logger.info("Initializing code understanding components...")

        # Create indexers
        code_indexer = CodebaseIndexer(collection_name="marunochithe_codebase")
        keyword_indexer = KeywordIndexer()

        # Create hybrid searcher
        hybrid_searcher = HybridSearcher(
            vector_indexer=code_indexer,
            keyword_indexer=keyword_indexer,
            rrf_k=60
        )

        logger.info("Code understanding components ready")
    except Exception as e:
        logger.warning(f"Code understanding initialization failed: {e}")
        logger.warning("Server will run without code search capabilities")

    # Initialize BenchAI client for multi-agent integration
    try:
        logger.info("Initializing BenchAI client...")
        # BenchAI client uses config automatically (no arguments needed)
        benchai_client = BenchAIClient()

        # Check if BenchAI is available
        benchai_available = await benchai_client.health_check()
        if benchai_available:
            logger.info("BenchAI client ready - multi-agent integration enabled")
        else:
            logger.info("BenchAI not available - will operate independently")
    except Exception as e:
        logger.warning(f"BenchAI client initialization failed: {e}")
        logger.warning("Server will run without multi-agent integration")

    logger.info("MarunochiAI server ready")

    yield

    logger.info("Shutting down MarunochiAI server...")

    # Cleanup code watcher if running
    if code_watcher:
        code_watcher.stop_watching()


# Create FastAPI app
app = FastAPI(
    title="MarunochiAI",
    description="The most powerful self-hosted coding assistant with A2A integration",
    version="0.2.0",
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
            version="0.2.0",
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return HealthResponse(
            status="unhealthy",
            ollama_available=False,
            models_loaded=[],
            version="0.2.0",
        )


@app.post("/v1/chat/completions", response_model=None)
async def chat_completions(
    request: ChatCompletionRequest
):
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

            yield f"data: {json.dumps(chunk_data)}\n\n"

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
        yield f"data: {json.dumps(final_chunk)}\n\n"
        yield "data: [DONE]\n\n"

    except Exception as e:
        logger.error(f"Streaming failed: {e}")
        error_chunk = {"error": str(e)}
        yield f"data: {json.dumps(error_chunk)}\n\n"


@app.post("/v1/codebase/index", tags=["Code Understanding"])
async def index_codebase(codebase_path: str, watch: bool = False) -> Dict:
    """
    Index entire codebase for semantic search.

    Args:
        codebase_path: Path to codebase directory
        watch: If True, start filesystem watcher for incremental updates

    Returns:
        Statistics about indexing operation
    """
    global code_indexer, code_watcher

    if not code_indexer:
        raise HTTPException(
            status_code=503,
            detail="Code understanding not initialized"
        )

    try:
        logger.info(f"Indexing codebase: {codebase_path}")

        # Index codebase
        result = await code_indexer.index_codebase(codebase_path)

        # Start watcher if requested
        if watch and not code_watcher:
            logger.info("Starting filesystem watcher...")

            parser = CodeParser()
            chunker = CodeChunker()
            keyword_indexer = hybrid_searcher.keyword_indexer

            code_watcher = CodebaseWatcher(
                codebase_path=codebase_path,
                vector_indexer=code_indexer,
                keyword_indexer=keyword_indexer,
                debounce_ms=500
            )

            await code_watcher.start_watching()
            result['watcher_started'] = True

        return result

    except Exception as e:
        logger.error(f"Indexing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/v1/codebase/search", tags=["Code Understanding"])
async def codebase_search(
    request: CodebaseSearchRequest
) -> CodebaseSearchResponse:
    """
    Semantic code search using hybrid vector + keyword search.

    Args:
        request: Search request with query and parameters

    Returns:
        Matching code chunks with similarity scores
    """
    if not hybrid_searcher:
        raise HTTPException(
            status_code=503,
            detail="Code understanding not initialized"
        )

    try:
        logger.debug(f"Searching codebase: {request.query}")

        # Perform hybrid search
        results = await hybrid_searcher.search(
            query=request.query,
            mode="hybrid",
            limit=request.limit
        )

        # Convert to API response format
        search_results = [
            CodebaseSearchResult(
                filepath=r.filepath,
                content=r.content,
                similarity=r.similarity,
                metadata={
                    'name': r.name,
                    'language': r.language.value,
                    'chunk_type': r.chunk_type,
                    'line_range': list(r.line_range),
                }
            )
            for r in results
        ]

        return CodebaseSearchResponse(
            query=request.query,
            results=search_results,
            total=len(search_results)
        )

    except Exception as e:
        logger.error(f"Search failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/v1/codebase/stats", tags=["Code Understanding"])
async def codebase_stats() -> Dict:
    """
    Get code understanding statistics.

    Returns:
        Indexing and search statistics
    """
    if not hybrid_searcher:
        raise HTTPException(
            status_code=503,
            detail="Code understanding not initialized"
        )

    try:
        stats = await hybrid_searcher.get_stats()

        # Add watcher status
        stats['watcher_running'] = code_watcher is not None and code_watcher._running

        return stats

    except Exception as e:
        logger.error(f"Stats retrieval failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/v1/codebase/refresh", tags=["Code Understanding"])
async def refresh_index(filepath: Optional[str] = None) -> Dict:
    """
    Refresh code index for a file or entire codebase.

    Args:
        filepath: Specific file to refresh, or None for full refresh

    Returns:
        Refresh operation result
    """
    if not code_indexer:
        raise HTTPException(
            status_code=503,
            detail="Code understanding not initialized"
        )

    try:
        if filepath:
            # Refresh single file
            logger.info(f"Refreshing index for: {filepath}")
            result = await code_indexer.index_file(filepath)
            return {
                'filepath': filepath,
                'chunks_indexed': result.get('indexed_chunks', 0),
                'duration_ms': result.get('duration_ms', 0)
            }
        else:
            # Full refresh - clear and reindex
            logger.info("Performing full index refresh")
            await code_indexer.clear_index()

            # Note: User needs to call /index again with codebase path
            return {
                'status': 'cleared',
                'message': 'Index cleared. Call /v1/codebase/index to reindex.'
            }

    except Exception as e:
        logger.error(f"Refresh failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# A2A Integration Endpoints


@app.post("/v1/sync/receive", tags=["A2A Integration"])
async def receive_sync_data(request: SyncRequest) -> SyncResponse:
    """
    Receive sync data from BenchAI or other agents.

    This endpoint allows other agents to push experiences, knowledge,
    and patterns to MarunochiAI for bidirectional learning.

    Args:
        request: Sync request with items to store

    Returns:
        Status and count of items processed
    """
    items_processed = 0

    for item in request.items:
        try:
            if request.sync_type == "experience":
                # Store coding experience
                logger.info(
                    f"Received experience from {request.from_agent}: "
                    f"{item.get('content', '')[:100]}..."
                )
                # TODO: Add to local experience storage (Phase 4)
                items_processed += 1

            elif request.sync_type == "knowledge":
                # Store knowledge note
                logger.info(
                    f"Received knowledge from {request.from_agent}: "
                    f"{item.get('title', '')}"
                )
                # TODO: Add to local knowledge storage (Phase 4)
                items_processed += 1

            elif request.sync_type == "pattern":
                # Store coding pattern
                logger.info(
                    f"Received pattern from {request.from_agent}: "
                    f"{item.get('pattern_name', '')}"
                )
                # TODO: Add to pattern library (Phase 4)
                items_processed += 1

        except Exception as e:
            logger.error(f"Failed to process sync item: {e}")
            continue

    return SyncResponse(
        status="ok",
        from_agent=request.from_agent,
        items_processed=items_processed,
        sync_type=request.sync_type
    )


@app.get("/v1/sync/share", tags=["A2A Integration"])
async def share_sync_data(
    requester: str,
    sync_type: str = "experience",
    since: Optional[str] = None,
    limit: int = 50
) -> ShareResponse:
    """
    Share data with BenchAI or other agents.

    This endpoint allows other agents to pull experiences, knowledge,
    and patterns from MarunochiAI.

    Args:
        requester: Agent requesting the data
        sync_type: Type of data to share (experience, knowledge, pattern)
        since: Timestamp to filter items (optional)
        limit: Maximum number of items to return

    Returns:
        List of items to share
    """
    items = []

    try:
        if sync_type == "experience":
            # Get recent successful coding experiences
            # TODO: Pull from actual experience storage (Phase 4)
            # For now, return placeholder
            items = [
                {
                    "id": "exp-001",
                    "content": "Successfully used hybrid search for code refactoring",
                    "importance": 4,
                    "category": "refactoring",
                    "created_at": "2025-12-26T12:00:00Z"
                }
            ]

        elif sync_type == "knowledge":
            # Get coding patterns and best practices learned
            # TODO: Pull from actual knowledge storage (Phase 4)
            items = [
                {
                    "id": "know-001",
                    "title": "Hybrid Search Best Practices",
                    "content": "RRF with k=60 provides optimal balance between vector and keyword search",
                    "tags": ["search", "rag", "optimization"]
                }
            ]

        elif sync_type == "pattern":
            # Get coding patterns
            # TODO: Pull from pattern library (Phase 4)
            items = []

    except Exception as e:
        logger.error(f"Failed to get sync data: {e}")

    return ShareResponse(
        status="ok",
        for_agent=requester,
        sync_type=sync_type,
        items=items,
        count=len(items)
    )


@app.post("/v1/a2a/task", tags=["A2A Integration"])
async def receive_task(request: A2ATaskRequest) -> A2ATaskResponse:
    """
    Receive a task from BenchAI or other agents.

    This endpoint processes coding tasks delegated by the orchestrator,
    leveraging MarunochiAI's code understanding capabilities.

    Args:
        request: Task request with type, description, and context

    Returns:
        Task result or status
    """
    task_id = f"maru-{uuid.uuid4().hex[:12]}"

    # Log task receipt
    logger.info(
        f"Received task from {request.from_agent}: "
        f"{request.task_description[:100]}..."
    )

    # Extract context from enriched A2A context
    knowledge_context = ""
    if request.context:
        knowledge = request.context.get("knowledge", {})
        embedded = knowledge.get("embedded_knowledge", [])
        for item in embedded:
            knowledge_context += f"\n{item.get('content', '')}"

    try:
        start_time = time.time()

        # Process based on task type
        if request.task_type == "code_search":
            # Use hybrid searcher
            if not hybrid_searcher:
                return A2ATaskResponse(
                    task_id=task_id,
                    status="failed",
                    message="Code search not available"
                )

            results = await hybrid_searcher.search(
                query=request.task_description,
                mode="hybrid",
                limit=10
            )

            duration_ms = (time.time() - start_time) * 1000

            # Report success to BenchAI
            if benchai_client:
                await benchai_client.report_task_completion(
                    task_type="code_search",
                    success=True,
                    metrics={
                        "duration_ms": duration_ms,
                        "results_count": len(results),
                        "from_agent": request.from_agent
                    },
                    description=f"Completed code search: {request.task_description[:100]}"
                )

            return A2ATaskResponse(
                task_id=task_id,
                status="completed",
                result={
                    "query": request.task_description,
                    "results": [
                        {
                            "filepath": r.filepath,
                            "name": r.name,
                            "content": r.content,
                            "similarity": r.similarity,
                            "line_range": list(r.line_range)
                        }
                        for r in results
                    ],
                    "count": len(results)
                }
            )

        elif request.task_type in ["code_completion", "code_review", "debugging", "refactoring"]:
            # Use chat completion with context
            messages = [
                {
                    "role": "system",
                    "content": f"You are a coding expert. Context: {knowledge_context}"
                },
                {
                    "role": "user",
                    "content": request.task_description
                }
            ]

            response = await engine.chat(messages=messages, stream=False)

            duration_ms = (time.time() - start_time) * 1000

            # Report success to BenchAI
            if benchai_client:
                await benchai_client.report_task_completion(
                    task_type=request.task_type,
                    success=True,
                    metrics={
                        "duration_ms": duration_ms,
                        "response_length": len(response),
                        "from_agent": request.from_agent
                    },
                    description=f"Completed {request.task_type}: {request.task_description[:100]}"
                )

            return A2ATaskResponse(
                task_id=task_id,
                status="completed",
                result={"response": response}
            )

        else:
            return A2ATaskResponse(
                task_id=task_id,
                status="pending",
                message=f"Task queued for processing"
            )

    except Exception as e:
        logger.error(f"Task processing failed: {e}")

        # Report failure to BenchAI
        if benchai_client:
            await benchai_client.report_task_completion(
                task_type=request.task_type,
                success=False,
                metrics={
                    "error": str(e),
                    "from_agent": request.from_agent
                },
                description=f"Failed {request.task_type}: {str(e)}"
            )

        return A2ATaskResponse(
            task_id=task_id,
            status="failed",
            message=str(e)
        )


@app.get("/.well-known/agent.json", tags=["A2A Integration"])
async def agent_card(request: Request):
    """
    A2A Agent Card for discovery.

    This endpoint provides agent capabilities and endpoints for
    multi-agent orchestration (A2A Protocol v0.3).

    Endpoints are dynamically generated based on the request host,
    ensuring correct URLs for cross-network communication.
    """
    # Build base URL from request (handles both localhost and network IP access)
    scheme = request.headers.get("x-forwarded-proto", "http")
    host = request.headers.get("host", "localhost:8765")
    base_url = f"{scheme}://{host}"

    return {
        "name": "MarunochiAI",
        "version": "0.2.0",
        "description": "The most powerful self-hosted coding assistant",
        "capabilities": [
            "code_search",
            "code_completion",
            "code_refactoring",
            "code_debugging",
            "test_generation",
            "code_explanation",
            "hybrid_search",
            "codebase_indexing"
        ],
        "domains": ["coding"],
        "priority": 0.95,
        "endpoints": {
            "health": f"{base_url}/health",
            "chat": f"{base_url}/v1/chat/completions",
            "search": f"{base_url}/v1/codebase/search",
            "index": f"{base_url}/v1/codebase/index",
            "stats": f"{base_url}/v1/codebase/stats",
            "sync_receive": f"{base_url}/v1/sync/receive",
            "sync_share": f"{base_url}/v1/sync/share",
            "a2a_task": f"{base_url}/v1/a2a/task"
        },
        "status": "online",
        "load": 0.0
    }


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "MarunochiAI",
        "version": "0.2.0",
        "description": "The most powerful self-hosted coding assistant",
        "endpoints": {
            "health": "/health",
            "chat": "/v1/chat/completions",
            "codebase_index": "/v1/codebase/index",
            "codebase_search": "/v1/codebase/search",
            "codebase_stats": "/v1/codebase/stats",
            "codebase_refresh": "/v1/codebase/refresh",
            "agent_card": "/.well-known/agent.json",
            "sync_receive": "/v1/sync/receive",
            "sync_share": "/v1/sync/share",
            "a2a_task": "/v1/a2a/task"
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
