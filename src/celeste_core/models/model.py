from __future__ import annotations

from pydantic import BaseModel, field_serializer

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider


class Model(BaseModel):
    """Model metadata with provider and capability flags.

    This is additive metadata and does not change provider behavior.
    """

    id: str
    provider: Provider
    capabilities: Capability = Capability.NONE
    display_name: str | None = None

    def supports(self, cap: Capability) -> bool:
        return bool(self.capabilities & cap)

    def supports_all(self, caps: Capability) -> bool:
        return (self.capabilities & caps) == caps

    @field_serializer("capabilities")
    def _serialize_capabilities(self, cap: Capability) -> list[str]:
        return [c.name for c in Capability if c and (c & cap)]


__all__ = ["Model"]
