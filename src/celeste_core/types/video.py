from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class VideoArtifact(BaseModel):
    """Represents a generated video artifact.

    Contains either a downloadable URL or raw bytes path reference.
    """

    url: Optional[str] = None
    path: Optional[str] = None
