from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.types.image import ImageArtifact
from celeste_core.validation import validate_client_config


class BaseImageEditor(ABC):
    def __init__(
        self, model: str, provider: Provider | None = None, **kwargs: Any
    ) -> None:
        """Initialize image editor with validation logic."""
        validate_client_config(model, provider, Capability.IMAGE_EDIT)
        self.model = model

    @abstractmethod
    async def edit_image(
        self, prompt: str, image: ImageArtifact, **kwargs: Any
    ) -> ImageArtifact:
        """Submit a request to start an image editing job."""
        raise NotImplementedError
