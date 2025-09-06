from __future__ import annotations

from pydantic import BaseModel


class AudioArtifact(BaseModel):
    """Represents a generated audio artifact.

    Contains either a downloadable URL, raw bytes data, or file path reference.
    """

    url: str | None = None
    data: bytes | None = None
    path: str | None = None
    format: str | None = None  # e.g., "wav", "mp3", "ogg"
    sample_rate: int | None = None  # e.g., 22050, 44100
    channels: int | None = None  # 1 for mono, 2 for stereo
