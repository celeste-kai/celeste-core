from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.image import ImageArtifact
from celeste_core.validation import validate_client_config


class BaseImageGenerator(ABC):
    def __init__(
        self, model: str, provider: Provider | None = None, **kwargs: Any
    ) -> None:
        """Initialize image generator with validation logic."""
        validate_client_config(model, provider, Capability.IMAGE_GENERATION)
        self.model_name = model

    @abstractmethod
    async def generate_image(self, prompt: str, **kwargs: Any) -> List[ImageArtifact]:
        """Submit a request to start an image generation job."""
        raise NotImplementedError
