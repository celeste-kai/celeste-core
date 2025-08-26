from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.image import ImageArtifact
from celeste_core.validation import validate_client_config


class BaseImageEnhancer(ABC):
    def __init__(
        self, model: str, provider: Provider | None = None, **kwargs: Any
    ) -> None:
        """Initialize image enhancer with validation logic."""
        validate_client_config(model, provider, Capability.IMAGE_ENHANCE)
        self.model = model

    @abstractmethod
    async def enhance_image(self, image: ImageArtifact, **kwargs: Any) -> ImageArtifact:
        """Submit a request to enhance an image."""
        raise NotImplementedError
