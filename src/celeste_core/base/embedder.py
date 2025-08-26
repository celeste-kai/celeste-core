from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterable, Union

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.response import AIResponse
from celeste_core.validation import validate_client_config


class BaseEmbedder(ABC):
    def __init__(
        self, model: str, provider: Provider | None = None, **kwargs: Any
    ) -> None:
        """Initialize embedder with validation logic."""
        validate_client_config(model, provider, Capability.EMBEDDINGS)
        self.model_name = model

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
