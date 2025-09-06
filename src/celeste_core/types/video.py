from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class VideoArtifact(BaseModel):
    """Represents a generated video artifact.

    Contains either a downloadable URL, raw bytes, or file path reference.
    """

    url: str | None = None
    path: str | None = None
    data: bytes | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
