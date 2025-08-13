from __future__ import annotations

from typing import Any, Dict, Generic, Optional, TypeVar

from celeste_core.enums.providers import Provider
from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class AIResponse(BaseModel, Generic[T]):
    """Generic AI response wrapper used across domains.

    The content type parameter T allows domains to specify their payloads:
    - Text: str | BaseModel | list[BaseModel]
    - Embeddings: list[Embedding]
    - Images: list[ImageArtifact]
    - Audio/doc: str
    """

    model_config = ConfigDict(frozen=True)

    content: T

    provider: Optional[Provider] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
