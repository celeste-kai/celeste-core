from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.registry import supports


class BaseClient(ABC):
    def __init__(
        self,
        model: str,
        capability: Capability = Capability.TEXT_GENERATION,
        provider: Provider | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize provider client with common validation logic."""
        self.model_name = model
        if provider is None:
            raise ValueError("provider is required for capability validation")
        if not supports(provider, self.model_name, capability):
            raise ValueError(
                f"Model '{self.model_name}' does not support {capability} "
                f"for provider {provider.value}"
            )

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
