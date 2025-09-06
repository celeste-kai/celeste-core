# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`celeste-core` is the foundational package for the Celeste multi-modal AI framework. It provides:

- **Model Catalog**: Centralized, editable registry of AI models from all providers (`catalog.py`)
- **Capability System**: Bitwise flags to describe what models can do (`Capability` enum)
- **Base Classes**: Abstract interfaces for all domain-specific clients (text, images, audio, etc.)
- **Validation**: Runtime checks to ensure models support requested capabilities
- **Configuration**: Unified settings management for all provider API keys

## Development Commands

### Testing
```bash
pytest tests/              # Run tests
pytest tests/test_settings.py -v  # Run specific test with verbose output
```

### Code Quality
```bash
uv run ruff check .        # Lint code
uv run ruff format .       # Format code
uv run mypy .             # Type checking
```

### Installation
```bash
uv pip install -e .       # Install in editable mode
```

## Core Architecture

### Model Catalog System
- **`models/catalog.py`**: The authoritative list of all models with capabilities
- **`models/registry.py`**: Query interface - `list_models()`, `get_model()`, `supports()`
- **`models/model.py`**: `Model` dataclass definition

### Capability-Based Validation
Models are annotated with capability flags from `enums/capability.py`:
```python
Capability.TEXT_GENERATION | Capability.VISION | Capability.STRUCTURED_OUTPUT
```

The validation system in `validation.py` ensures clients only use models that support required capabilities.

### Base Client Architecture
All domain packages inherit from base classes in `base/`:
- `client.py` - Text generation base
- `image_generator.py` - Image generation base
- `embedder.py` - Embeddings base
- And specialized bases for audio, video, documents, etc.

### Provider Configuration
`config/settings.py` manages API credentials for all providers:
- OpenAI, Anthropic, Google, Mistral, HuggingFace
- Ollama, Stability AI, Luma, xAI, Replicate, Cohere, Topaz Labs
- Uses Pydantic with `.env` file loading

## Adding New Models

1. Add model entry to `CATALOG` in `catalog.py`:
```python
Model(
    id="model-name",
    provider=Provider.PROVIDER_NAME,
    capabilities=Capability.CAPABILITY_1 | Capability.CAPABILITY_2,
    display_name="Display Name",
)
```

2. Ensure provider enum exists in `enums/providers.py`
3. Update provider mapping in relevant domain package
4. Add provider settings to `config/settings.py` if needed

## Key Files

- `src/celeste_core/models/catalog.py` - Master model list (580+ lines)
- `src/celeste_core/enums/capability.py` - Capability flag definitions
- `src/celeste_core/validation.py` - Client validation logic
- `src/celeste_core/config/settings.py` - Provider credential management
- `src/celeste_core/base/` - Abstract base classes for all domains
