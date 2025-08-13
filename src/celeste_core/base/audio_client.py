from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.registry import supports


class BaseAudioClient(ABC):
    def __init__(
        self,
        model: str,
        capability: Capability = Capability.AUDIO_TRANSCRIPTION,
        provider: Provider | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize audio client with validation logic."""
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
        self, prompt: str, audio_file: Any, **kwargs: Any
    ) -> Any:
        """Generate a single response from a prompt and an audio input."""
        raise NotImplementedError

    @abstractmethod
    def stream_generate_content(
        self, prompt: str, audio_file: Any, **kwargs: Any
    ) -> AsyncIterator[Any]:
        """Stream the response chunk by chunk."""
        raise NotImplementedError
