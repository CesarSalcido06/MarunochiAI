"""Ollama inference engine with intelligent 7B/14B routing."""

import asyncio
from enum import Enum
from typing import AsyncIterator, Dict, List, Optional, Union
from loguru import logger
import ollama


class ModelSize(str, Enum):
    """Model size selection."""
    FAST = "qwen2.5-coder:7b"  # 47 t/s, 1.5-3s responses
    POWERFUL = "qwen2.5-coder:14b"  # 25 t/s, 4-8s responses
    CUSTOM = "marunochithe-custom"  # Fine-tuned model


class TaskComplexity(Enum):
    """Task complexity classification."""
    SIMPLE = "simple"  # Quick completions, inline edits
    COMPLEX = "complex"  # Multi-file refactoring, architecture


class InferenceEngine:
    """
    Intelligent inference engine with automatic model selection.

    Routes tasks to 7B (fast) or 14B (powerful) based on complexity analysis.
    """

    def __init__(
        self,
        ollama_host: str = "http://localhost:11434",
        default_model: ModelSize = ModelSize.FAST,
        enable_custom: bool = False,
    ):
        """
        Initialize inference engine.

        Args:
            ollama_host: Ollama server endpoint
            default_model: Default model to use
            enable_custom: Use fine-tuned custom model if available
        """
        self.ollama_host = ollama_host
        self.default_model = default_model
        self.enable_custom = enable_custom
        self.client = ollama.AsyncClient(host=ollama_host)

        # Complexity keywords for routing
        self.complex_keywords = {
            "refactor", "architecture", "optimize", "redesign", "implement",
            "algorithm", "data structure", "performance", "scalability",
            "design pattern", "multi-file", "entire", "complex", "advanced"
        }
        self.simple_keywords = {
            "simple", "quick", "small", "inline", "autocomplete", "complete",
            "fix typo", "add comment", "format", "style"
        }

    def _analyze_complexity(self, prompt: str, context: Optional[Dict] = None) -> TaskComplexity:
        """
        Analyze task complexity to choose appropriate model.

        Args:
            prompt: User request
            context: Additional context (file content, etc.)

        Returns:
            TaskComplexity classification
        """
        prompt_lower = prompt.lower()

        # Check for simple keywords first (bias toward speed)
        if any(kw in prompt_lower for kw in self.simple_keywords):
            return TaskComplexity.SIMPLE

        # Check for complex keywords
        complex_score = sum(1 for kw in self.complex_keywords if kw in prompt_lower)

        # Long prompts likely complex
        if len(prompt) > 500:
            complex_score += 1

        # Multi-file context indicates complexity
        if context and len(context.get("files", [])) > 1:
            complex_score += 1

        return TaskComplexity.COMPLEX if complex_score >= 2 else TaskComplexity.SIMPLE

    def _select_model(self, complexity: TaskComplexity) -> ModelSize:
        """
        Select model based on task complexity.

        Args:
            complexity: Classified task complexity

        Returns:
            Selected model
        """
        # Use custom model if available and enabled
        if self.enable_custom:
            try:
                # Check if custom model exists
                models = ollama.list()
                if any(m["name"] == ModelSize.CUSTOM for m in models.get("models", [])):
                    logger.info("Using fine-tuned custom model")
                    return ModelSize.CUSTOM
            except Exception as e:
                logger.warning(f"Custom model check failed: {e}")

        # Route based on complexity
        if complexity == TaskComplexity.SIMPLE:
            logger.debug("Routing to 7B (fast model)")
            return ModelSize.FAST
        else:
            logger.debug("Routing to 14B (powerful model)")
            return ModelSize.POWERFUL

    async def chat(
        self,
        messages: List[Dict[str, str]],
        model: Optional[ModelSize] = None,
        stream: bool = False,
        context: Optional[Dict] = None,
        **kwargs
    ) -> Union[str, AsyncIterator[str]]:
        """
        Generate chat completion with intelligent model selection.

        Args:
            messages: Chat messages (OpenAI format)
            model: Override automatic model selection
            stream: Stream response tokens
            context: Additional context for complexity analysis
            **kwargs: Additional Ollama parameters

        Returns:
            Generated text (or async iterator if streaming)
        """
        # Auto-select model if not specified
        if model is None:
            last_message = messages[-1]["content"] if messages else ""
            complexity = self._analyze_complexity(last_message, context)
            model = self._select_model(complexity)

        logger.info(f"Generating completion with {model}")

        try:
            if stream:
                return self._stream_chat(messages, model, **kwargs)
            else:
                response = await self.client.chat(
                    model=model,
                    messages=messages,
                    **kwargs
                )
                return response["message"]["content"]

        except Exception as e:
            logger.error(f"Inference failed: {e}")

            # Fallback to smaller model on error
            if model == ModelSize.POWERFUL:
                logger.warning("Falling back to 7B model")
                return await self.chat(messages, model=ModelSize.FAST, stream=stream, **kwargs)

            raise

    async def _stream_chat(
        self,
        messages: List[Dict[str, str]],
        model: ModelSize,
        **kwargs
    ) -> AsyncIterator[str]:
        """
        Stream chat completion tokens.

        Args:
            messages: Chat messages
            model: Selected model
            **kwargs: Additional parameters

        Yields:
            Generated tokens
        """
        async for chunk in await self.client.chat(
            model=model,
            messages=messages,
            stream=True,
            **kwargs
        ):
            if chunk["message"]["content"]:
                yield chunk["message"]["content"]

    async def complete(
        self,
        prompt: str,
        model: Optional[ModelSize] = None,
        **kwargs
    ) -> str:
        """
        Generate code completion (non-chat mode).

        Args:
            prompt: Code prefix
            model: Model override
            **kwargs: Additional parameters

        Returns:
            Completed code
        """
        if model is None:
            complexity = self._analyze_complexity(prompt)
            model = self._select_model(complexity)

        logger.info(f"Generating completion with {model}")

        response = await self.client.generate(
            model=model,
            prompt=prompt,
            **kwargs
        )

        return response["response"]

    async def health_check(self) -> bool:
        """
        Check if Ollama is healthy and models are available.

        Returns:
            True if healthy
        """
        try:
            models_response = await self.client.list()
            # Handle both new ListResponse object and legacy dict format
            if hasattr(models_response, 'models'):
                models = models_response.models
                model_names = [m.model for m in models]
            else:
                models = models_response.get("models", [])
                model_names = [m["name"] for m in models]

            has_7b = ModelSize.FAST in model_names
            has_14b = ModelSize.POWERFUL in model_names

            if not (has_7b and has_14b):
                logger.warning(f"Missing models. Available: {model_names}")
                return False

            logger.info("Ollama health check passed")
            return True

        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False
