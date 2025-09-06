from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.validation import validate_client_config


class BaseDocClient(ABC):
    def __init__(
        self,
        model: str,
        provider: Provider | None = None,
        **kwargs: Any,  # noqa: ARG002
    ) -> None:
        """Initialize document intelligence client with validation logic."""
        validate_client_config(model, provider, Capability.DOCUMENT_INTELLIGENCE)
        self.model = model

    @abstractmethod
    async def generate_content(self, prompt: str, documents: Any, **kwargs: Any) -> Any:
        """Generate a single response from prompt and documents."""
        raise NotImplementedError

    @abstractmethod
    async def stream_generate_content(self, prompt: str, documents: Any, **kwargs: Any) -> AsyncIterator[Any]:
        """Stream the response chunk by chunk."""
        raise NotImplementedError
