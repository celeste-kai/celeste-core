from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Union

from celeste_core.types.response import AIResponse


class BaseReranker(ABC):
    @abstractmethod
    def __init__(self, **kwargs: Any) -> None:  # pragma: no cover - interface only
        """Initialize provider reranker; provider-specific args via kwargs."""
        raise NotImplementedError

    @abstractmethod
    async def rerank(
        self, query: str, texts: Union[str, List[str]], top_k: int = 5, **kwargs: Any
    ) -> AIResponse[List[str]]:
        """Rerank texts based on relevance to query.

        Returns an AIResponse whose content is the reranked texts in relevance order.
        Scores and original indices are available in metadata.
        Single-string inputs return a list with a single text to keep the
        return shape consistent.
        """
        raise NotImplementedError
