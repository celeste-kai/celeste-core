from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, model_validator


class ImageArtifact(BaseModel):
    """Represents an image artifact and its metadata."""

    data: Optional[bytes] = None
    path: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _check_data_or_path(self) -> "ImageArtifact":
        if not (self.data or self.path):
            raise ValueError("Either 'data' or 'path' must be provided")
        return self
