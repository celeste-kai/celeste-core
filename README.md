<div align="center">

# 🧩 Celeste Core

### Core Types, Enums, Model Registry, and Base Interfaces for the Celeste Ecosystem

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Models](https://img.shields.io/badge/Models-Catalog-orange?style=for-the-badge&logo=bookstack&logoColor=white)](#-model-catalog)
[![Registry](https://img.shields.io/badge/Registry-Capability_Aware-purple?style=for-the-badge&logo=databricks&logoColor=white)](#-model-registry)

</div>

---

## 🎯 Why Celeste Core?

<div align="center">
  <table>
    <tr>
      <td align="center">🧱<br><b>Foundation</b><br>Shared types, enums, and base interfaces</td>
      <td align="center">📚<br><b>Model Catalog</b><br>Centralized, editable list of models</td>
      <td align="center">🎛️<br><b>Capability Flags</b><br>Filter models by what they can do</td>
      <td align="center">🔍<br><b>Registry</b><br>Query by provider/capability</td>
    </tr>
  </table>
</div>

`celeste-core` defines primitives shared across the Celeste ecosystem:
- Enums: `Capability`, `Provider`
- Types: `AIResponse`, `ImageArtifact`
- Model metadata: `Model` dataclass and the editable `CATALOG`
- Registry helpers: filter models by capability/provider and check support
- Base interfaces for domain clients (text, images, audio, docs, embeddings)

## 🚀 Quick Start

```bash
pip install -e .
```

List models by capability/provider:

```python
from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.registry import list_models

# All image generation models
image_models = list_models(capability=Capability.IMAGE_GENERATION)

# Google-only image generation models
google_image_models = list_models(
    capability=Capability.IMAGE_GENERATION,
    provider=Provider.GOOGLE,
)

for m in google_image_models:
    print(m.id, m.provider.value)
```

Check capability support on a model:

```python
from celeste_core.models.registry import supports
from celeste_core.enums.capability import Capability

assert supports("gemini-2.5-flash", Capability.TEXT_GENERATION)
```

## 📦 Installation

<details open>
<summary><b>Using pip</b></summary>

```bash
git clone https://github.com/yourusername/celeste
cd celeste/celeste-core
pip install -e .
```

</details>

<details>
<summary><b>Using UV</b></summary>

```bash
uv pip install -e .
```

</details>

## 🔧 Configuration

No configuration is required for `celeste-core` itself. Provider API keys are consumed by the specific provider packages, not by core.

## 🧭 Model Registry

Key functions from `celeste_core.models.registry`:
- `list_models(provider: Optional[Provider] = None, capability: Optional[Capability] = None) -> list[Model]`
- `get_model(model_id: str) -> Model | None`
- `supports(model_id: str, cap: Capability) -> bool`
- `reload_catalog() -> None` (re-seeds the registry from the Python `CATALOG`)

The registry is automatically loaded at import time from the Python catalog.

## 📖 Model Catalog

The editable model list lives in `celeste_core.models.catalog.CATALOG`. Each entry is a `Model`:

```python
from celeste_core.models.model import Model
from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider

Model(
    id="gemini-2.5-flash",
    provider=Provider.GOOGLE,
    capabilities=Capability.TEXT_GENERATION | Capability.STRUCTURED_OUTPUT | Capability.VISION,
    display_name="Gemini 2.5 Flash",
)
```

To add or tweak models:
- Add/modify a `Model` in `catalog.py`
- Set accurate `capabilities` using `Capability` flags
- Ensure `id` matches the provider library’s expected identifier
- Run `reload_catalog()` if needed (the module reloads on import by default)

## 🧱 Base Interfaces

Abstract base classes unify provider implementations across domains:
- `base/client.py` (text)
- `base/image_generator.py`
- `base/image_editor.py`
- `base/audio_client.py`
- `base/document_client.py`
- `base/embedder.py`

These define method signatures and return the shared `AIResponse` or domain types.

## 🗺️ Roadmap

- [ ] Expand `CATALOG` coverage and keep capability flags current
- [ ] Document conventions for model IDs and display names
- [ ] Add richer metadata (context window, pricing hints) when available
- [ ] Reintroduce cross‑modality usage accounting (tokens, images, audio seconds, pages) in a future iteration

## 🌌 Celeste Ecosystem

| Package | Description | Status |
|---------|-------------|--------|
| 🧩 **celeste-core** | Core types, enums, registry, base interfaces | 🔄 This Package |
| 💬 **celeste-client** | Text generation & chat | ✅ Available |
| 🎨 **celeste-image-generation** | Multi‑provider image gen | ✅ Available |
| ✏️ **celeste-image-edit** | Image editing | ✅ Available |
| 🎧 **celeste-audio-intelligence** | Audio processing | ✅ Available |
| 📄 **celeste-document-intelligence** | PDF/document QA | ✅ Available |
| 🔢 **celeste-embeddings** | Text embeddings | ✅ Available |
| 🌐 **celeste-api** | REST/SSE API for UI | 🔄 In Progress |
| 🖥️ **celeste-ui** | React/Next.js front‑end | 🔄 In Progress |

## 🤝 Contributing

We welcome contributions! Please open issues/PRs to add models, improve capability flags, or propose new core types.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

<div align="center">
  Made with ❤️ by the Celeste Team

  <a href="#-celeste-core">⬆ Back to Top</a>
</div>
