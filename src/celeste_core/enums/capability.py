"""Capability flags used to annotate model features.

These flags are combinable with bitwise operations. Use to describe what a
given model can do (e.g., text generation, embeddings, image edit, etc.).
"""

from enum import IntFlag


class Capability(IntFlag):
    NONE = 0
    TEXT_GENERATION = 1 << 0
    IMAGE_GENERATION = 1 << 1
    IMAGE_EDIT = 1 << 2
    AUDIO_TRANSCRIPTION = 1 << 3
    AUDIO_GENERATION = 1 << 4
    EMBEDDINGS = 1 << 5
    DOCUMENT_INTELLIGENCE = 1 << 6
    VIDEO_GENERATION = 1 << 7
    STRUCTURED_OUTPUT = 1 << 8
    FUNCTION_CALLING = 1 << 9
    VISION = 1 << 10
    RERANKING = 1 << 11
    IMAGE_ENHANCE = 1 << 12
    TEXT_TO_SPEECH = 1 << 13


__all__ = ["Capability"]
