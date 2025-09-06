from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.image import ImageArtifact
from celeste_core.validation import validate_client_config


class BaseVideoClient(ABC):
    def __init__(
        self,
        model: str,
        provider: Provider | None = None,
        **kwargs: Any,  # noqa: ARG002
    ) -> None:
        """Initialize video generation client with validation logic."""
        validate_client_config(model, provider, Capability.VIDEO_GENERATION)
        self.model = model

    @abstractmethod
    async def generate_content(self, prompt: str, image: ImageArtifact | None = None, **kwargs: Any) -> Any:
        """Generate a video from a prompt and return domain-specific response."""
        raise NotImplementedError
