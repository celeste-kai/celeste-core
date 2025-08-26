from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.audio import AudioArtifact
from celeste_core.validation import validate_client_config


class BaseTTSClient(ABC):
    def __init__(
        self, model: str, provider: Provider | None = None, **kwargs: Any
    ) -> None:
        """Initialize TTS client with validation logic."""
        validate_client_config(model, provider, Capability.TEXT_TO_SPEECH)
        self.model_name = model

    @abstractmethod
    async def generate_speech(
        self, text: str, voice_name: str, **kwargs: Any
    ) -> AudioArtifact:
        """Generate speech audio from text with specified voice."""
        raise NotImplementedError
