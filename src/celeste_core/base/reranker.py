from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.response import AIResponse
from celeste_core.validation import validate_client_config


class BaseReranker(ABC):
    def __init__(self, model: str, provider: Provider | None = None, **kwargs: Any) -> None:  # noqa: ARG002
        """Initialize reranker with validation logic."""
        validate_client_config(model, provider, Capability.RERANKING)
        self.model = model

    @abstractmethod
    async def rerank(self, query: str, texts: str | list[str], top_k: int = 5, **kwargs: Any) -> AIResponse[list[str]]:
        """Rerank texts based on relevance to query.

        Returns an AIResponse whose content is the reranked texts in relevance order.
        Scores and original indices are available in metadata.
        Single-string inputs return a list with a single text to keep the
        return shape consistent.
        """
        raise NotImplementedError
