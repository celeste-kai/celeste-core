from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.response import AIResponse
from celeste_core.validation import validate_client_config


class BaseEmbedder(ABC):
    def __init__(self, model: str, provider: Provider | None = None, **kwargs: Any) -> None:  # noqa: ARG002
        """Initialize embedder with validation logic."""
        validate_client_config(model, provider, Capability.EMBEDDINGS)
        self.model = model

    @abstractmethod
    async def generate_embeddings(self, texts: str | Iterable[str], **kwargs: Any) -> AIResponse:
        """Generate embeddings for the given text(s).

        Returns an AIResponse whose content is a 2D list of floats
        (List[List[float]]). Single-string inputs return a list with a single
        vector to keep the return shape consistent.
        """
        raise NotImplementedError
