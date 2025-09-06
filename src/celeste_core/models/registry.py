from __future__ import annotations

from collections.abc import Iterable

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.model import Model

# Central registry mapping (provider, model_id) to metadata.
MODEL_REGISTRY: dict[tuple[Provider, str], Model] = {}


def register_model(model: Model) -> None:
    """Register or update a model entry in the registry."""
    MODEL_REGISTRY[(model.provider, model.id)] = model


def clear_registry() -> None:
    """Clear all registered models."""
    MODEL_REGISTRY.clear()


def get_model(provider: Provider, model_id: str) -> Model | None:
    return MODEL_REGISTRY.get((provider, model_id))


def list_models(*, provider: Provider | None = None, capability: Capability | None = None) -> list[Model]:
    models: Iterable[Model] = MODEL_REGISTRY.values()
    if provider is not None:
        models = (m for m in models if m.provider == provider)
    if capability is not None:
        models = (m for m in models if m.supports(capability))
    return list(models)


def list_providers(*, capability: Capability | None = None) -> list[Provider]:
    """Return distinct providers, optionally filtered by capability support.

    When capability is provided, only providers that have at least one model
    supporting the capability are returned.
    """
    if capability is None:
        return sorted(
            {provider for (provider, _model_id) in MODEL_REGISTRY},
            key=lambda p: p.value,
        )

    supported_models = list_models(capability=capability)
    providers = {m.provider for m in supported_models}
    return sorted(providers, key=lambda p: p.value)


def supports(provider: Provider, model_id: str, cap: Capability) -> bool:
    model = get_model(provider, model_id)
    return bool(model and model.supports(cap))


# -----------------------------
# Seed registry with known models
# -----------------------------


def reload_catalog() -> None:
    """Reload the built-in Python catalog into the registry."""
    from celeste_core.models.catalog import CATALOG  # noqa: PLC0415

    clear_registry()
    for model in CATALOG:
        register_model(model)


__all__ = [
    "MODEL_REGISTRY",
    "get_model",
    "list_models",
    "list_providers",
    "supports",
    "register_model",
    "clear_registry",
    "reload_catalog",
]

# Load built-in catalog on import so the registry is usable by default.
reload_catalog()
