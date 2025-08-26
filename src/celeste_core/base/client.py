from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.validation import validate_client_config


class BaseClient(ABC):
    def __init__(
        self,
        model: str,
        provider: Provider | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize text generation client with validation logic."""
        validate_client_config(model, provider, Capability.TEXT_GENERATION)
        self.model = model

    @abstractmethod
    async def generate_content(
        self, prompt: str, **kwargs: Any
    ) -> Any:  # domain returns its own response type
        """Generate a single response."""
        raise NotImplementedError

    @abstractmethod
    async def stream_generate_content(
        self, prompt: str, **kwargs: Any
    ) -> AsyncIterator[Any]:
        """Stream the response chunk by chunk."""
        raise NotImplementedError
