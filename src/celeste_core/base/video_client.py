from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.registry import supports


class BaseVideoClient(ABC):
    def __init__(
        self,
        model: str,
        capability: Capability = Capability.VIDEO_GENERATION,
        provider: Provider | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize provider client with validation for video capability."""
        self.model_name = model
        if provider is None:
            raise ValueError("provider is required for capability validation")
        if not supports(provider, self.model_name, capability):
            raise ValueError(
                f"Model '{self.model_name}' does not support {capability} "
                f"for provider {provider.value}"
            )

    @abstractmethod
    async def generate_content(self, prompt: str, **kwargs: Any) -> Any:
        """Generate a video from a prompt and return domain-specific response."""
        raise NotImplementedError
