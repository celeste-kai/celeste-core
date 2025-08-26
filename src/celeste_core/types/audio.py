from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class AudioArtifact(BaseModel):
    """Represents a generated audio artifact.

    Contains either a downloadable URL, raw bytes data, or file path reference.
    """

    url: Optional[str] = None
    data: Optional[bytes] = None
    path: Optional[str] = None
    format: Optional[str] = None  # e.g., "wav", "mp3", "ogg"
    sample_rate: Optional[int] = None  # e.g., 22050, 44100
    channels: Optional[int] = None  # 1 for mono, 2 for stereo
