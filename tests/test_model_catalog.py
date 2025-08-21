from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.catalog import CATALOG


def test_gemini_vision_models_have_document_intelligence():
    for model in CATALOG:
        if (
            model.provider == Provider.GOOGLE
            and model.id.startswith("gemini")
            and model.capabilities & Capability.VISION
        ):
            assert model.capabilities & Capability.DOCUMENT_INTELLIGENCE
