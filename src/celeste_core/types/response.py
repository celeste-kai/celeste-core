from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from celeste_core.enums.providers import Provider

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

    provider: Provider | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
