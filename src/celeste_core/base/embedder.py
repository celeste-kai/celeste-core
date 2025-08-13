from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterable, Union

from celeste_core.types.response import AIResponse


class BaseEmbedder(ABC):
    @abstractmethod
    def __init__(self, **kwargs: Any) -> None:  # pragma: no cover - interface only
        """Initialize provider embedder; provider-specific args via kwargs."""
        raise NotImplementedError

    @abstractmethod
    async def generate_embeddings(
        self, texts: Union[str, Iterable[str]], **kwargs: Any
    ) -> AIResponse:
        """Generate embeddings for the given text(s).

        Returns an AIResponse whose content is a 2D list of floats
        (List[List[float]]). Single-string inputs return a list with a single
        vector to keep the return shape consistent.
        """
        raise NotImplementedError
