"""Celeste Core: shared config, enums, base classes, and types."""

from .enums.capability import Capability
from .enums.providers import Provider
from .models.model import Model
from .models.registry import (
    MODEL_REGISTRY,
    clear_registry,
    get_model,
    list_models,
    register_model,
    reload_catalog,
    supports,
)
from .types.image import ImageArtifact
from .types.response import AIResponse
from .types.video import VideoArtifact

__all__ = [
    "Provider",
    "Capability",
    "AIResponse",
    "ImageArtifact",
    "VideoArtifact",
    "Model",
    "MODEL_REGISTRY",
    "get_model",
    "list_models",
    "supports",
    "register_model",
    "clear_registry",
    "reload_catalog",
]
