"""Client validation utilities for Celeste base classes."""

from __future__ import annotations

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.registry import supports


def validate_client_config(
    model: str, provider: Provider | None, capability: Capability
) -> None:
    """Validate client configuration (provider + model + capability support).

    Args:
        model: The model identifier to validate
        provider: The provider to use (must not be None)
        capability: The capability that must be supported

    Raises:
        ValueError: If provider is None or model doesn't support capability
    """
    if provider is None:
        raise ValueError("provider is required for client initialization")

    if not supports(provider, model, capability):
        capability_name = capability.name.lower().replace("_", " ")
        raise ValueError(
            f"Model '{model}' does not support {capability_name} "
            f"for provider {provider.value}"
        )
