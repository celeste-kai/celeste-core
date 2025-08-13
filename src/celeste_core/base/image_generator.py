from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List

from celeste_core.types.image import ImageArtifact


class BaseImageGenerator(ABC):
    def __init__(self, **kwargs: Any) -> None:  # pragma: no cover - interface only
        """Initialize image generator; provider-specific args via kwargs."""
        # Intentionally empty base init for forward compatibility
        return

    @abstractmethod
    async def generate_image(self, prompt: str, **kwargs: Any) -> List[ImageArtifact]:
        """Submit a request to start an image generation job."""
        raise NotImplementedError
