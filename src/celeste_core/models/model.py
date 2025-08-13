from __future__ import annotations

from typing import List, Optional

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from pydantic import BaseModel, field_serializer


class Model(BaseModel):
    """Model metadata with provider and capability flags.

    This is additive metadata and does not change provider behavior.
    """

    id: str
    provider: Provider
    capabilities: Capability = Capability.NONE
    display_name: Optional[str] = None

    def supports(self, cap: Capability) -> bool:
        return bool(self.capabilities & cap)

    def supports_all(self, caps: Capability) -> bool:
        return (self.capabilities & caps) == caps

    @field_serializer("capabilities")
    def _serialize_capabilities(self, cap: Capability) -> List[str]:
        return [c.name for c in Capability if c and (c & cap)]


__all__ = ["Model"]
