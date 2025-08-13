from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from celeste_core.types.image import ImageArtifact


class BaseImageEditor(ABC):
    @abstractmethod
    def __init__(self, **kwargs: Any) -> None:  # pragma: no cover - interface only
        """Initialize image editor; provider-specific args via kwargs."""
        raise NotImplementedError

    @abstractmethod
    async def edit_image(
        self, prompt: str, image: ImageArtifact, **kwargs: Any
    ) -> ImageArtifact:
        """Submit a request to start an image editing job."""
        raise NotImplementedError
