from __future__ import annotations

from typing import List

from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider
from celeste_core.models.model import Model

# Define models explicitly to keep per-model capabilities easy to tweak.
# Contributors can edit this list to add/update models.
CATALOG: List[Model] = [
    # OpenAI
    Model(
        id="dall-e-3",
        provider=Provider.OPENAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="DALL·E 3",
    ),
    Model(
        id="dall-e-2",
        provider=Provider.OPENAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="DALL·E 2",
    ),
    Model(
        id="gpt-image-1",
        provider=Provider.OPENAI,
        capabilities=Capability.IMAGE_GENERATION | Capability.IMAGE_EDIT,
        display_name="GPT-Image-1",
    ),
    Model(
        id="whisper-1",
        provider=Provider.OPENAI,
        capabilities=Capability.AUDIO_TRANSCRIPTION,
        display_name="Whisper 1",
    ),
    # Google
    Model(
        id="gemini-2.5-flash",
        provider=Provider.GOOGLE,
        capabilities=Capability.TEXT_GENERATION
        | Capability.STRUCTURED_OUTPUT
        | Capability.VISION,
        display_name="Gemini 2.5 Flash",
    ),
    Model(
        id="gemini-2.5-pro",
        provider=Provider.GOOGLE,
        capabilities=Capability.TEXT_GENERATION
        | Capability.STRUCTURED_OUTPUT
        | Capability.VISION,
        display_name="Gemini 2.5 Pro",
    ),
    Model(
        id="gemini-2.5-flash-lite-preview-06-17",
        provider=Provider.GOOGLE,
        capabilities=Capability.TEXT_GENERATION
        | Capability.STRUCTURED_OUTPUT
        | Capability.VISION
        | Capability.AUDIO_TRANSCRIPTION,
        display_name="Gemini 2.5 Flash Lite",
    ),
    Model(
        id="imagen-3.0-generate-002",
        provider=Provider.GOOGLE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Imagen 3",
    ),
    Model(
        id="imagen-4.0-generate-preview-06-06",
        provider=Provider.GOOGLE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Imagen 4 (preview)",
    ),
    Model(
        id="imagen-4.0-ultra-generate-preview-06-06",
        provider=Provider.GOOGLE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Imagen 4 Ultra (preview)",
    ),
    Model(
        id="gemini-embedding-exp-03-07",
        provider=Provider.GOOGLE,
        capabilities=Capability.EMBEDDINGS,
        display_name="Gemini Embeddings (exp-03-07)",
    ),
    Model(
        id="text-embedding-004",
        provider=Provider.GOOGLE,
        capabilities=Capability.EMBEDDINGS,
        display_name="Text Embeddings 004",
    ),
    Model(
        id="embedding-001",
        provider=Provider.GOOGLE,
        capabilities=Capability.EMBEDDINGS,
        display_name="Embeddings 001",
    ),
    # Mistral
    Model(
        id="mistral-embed",
        provider=Provider.MISTRAL,
        capabilities=Capability.EMBEDDINGS,
        display_name="Mistral Embeddings",
    ),
    Model(
        id="codestral-embed",
        provider=Provider.MISTRAL,
        capabilities=Capability.EMBEDDINGS,
        display_name="Codestral Embeddings",
    ),
    # xAI
    Model(
        id="grok-2-image",
        provider=Provider.XAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Grok-2 Image",
    ),
    # Luma
    Model(
        id="photon-1",
        provider=Provider.LUMA,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Photon 1",
    ),
    Model(
        id="photon-flash-1",
        provider=Provider.LUMA,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Photon Flash 1",
    ),
    # Stability AI
    Model(
        id="ultra",
        provider=Provider.STABILITYAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Ultra",
    ),
    Model(
        id="sd3.5-large",
        provider=Provider.STABILITYAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SD3.5 Large",
    ),
    Model(
        id="sd3.5-large-turbo",
        provider=Provider.STABILITYAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SD3.5 Large Turbo",
    ),
    Model(
        id="sd3.5-medium",
        provider=Provider.STABILITYAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SD3.5 Medium",
    ),
    Model(
        id="core",
        provider=Provider.STABILITYAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Core",
    ),
    Model(
        id="stable-diffusion-xl-1024-v1-0",
        provider=Provider.STABILITYAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SDXL 1.0",
    ),
    Model(
        id="stable-diffusion-v1-6",
        provider=Provider.STABILITYAI,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SD 1.6",
    ),
    # Hugging Face image models
    Model(
        id="black-forest-labs/FLUX.1-schnell",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="FLUX.1 Schnell",
    ),
    Model(
        id="black-forest-labs/FLUX.1-dev",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="FLUX.1 Dev",
    ),
    Model(
        id="black-forest-labs/FLUX.1-Krea-dev",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="FLUX.1 Krea Dev",
    ),
    Model(
        id="stabilityai/stable-diffusion-xl-base-1.0",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SDXL Base 1.0",
    ),
    Model(
        id="stabilityai/stable-diffusion-3-medium-diffusers",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SD3 Medium",
    ),
    Model(
        id="Qwen/Qwen-Image",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Qwen Image",
    ),
    # Local image models
    Model(
        id="stabilityai/sdxl-turbo",
        provider=Provider.LOCAL,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SDXL Turbo",
    ),
    Model(
        id="stabilityai/stable-diffusion-xl-base-1.0",
        provider=Provider.LOCAL,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SDXL Base 1.0",
    ),
    Model(
        id="stabilityai/stable-diffusion-2-1",
        provider=Provider.LOCAL,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="SD 2.1",
    ),
    # Image edit
    Model(
        id="gemini-2.0-flash-preview-image-generation",
        provider=Provider.GOOGLE,
        capabilities=Capability.IMAGE_EDIT,
        display_name="Gemini Flash 2.0 Preview (Image Gen)",
    ),
    Model(
        id="gemini-2.0-flash-exp-image-generation",
        provider=Provider.GOOGLE,
        capabilities=Capability.IMAGE_EDIT,
        display_name="Gemini Flash 2.0 Exp (Image Gen)",
    ),
    Model(
        id="gemini-2.0-flash-exp",
        provider=Provider.GOOGLE,
        capabilities=Capability.IMAGE_EDIT,
        display_name="Gemini Flash 2.0 Exp",
    ),
    Model(
        id="black-forest-labs/flux-kontext-pro",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_EDIT,
        display_name="FLUX Kontext Pro",
    ),
    Model(
        id="black-forest-labs/flux-kontext-max",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_EDIT,
        display_name="FLUX Kontext Max",
    ),
    # Replicate-hosted Qwen-Image (text-to-image only; no image edit input key exposed)
    Model(
        id="qwen/qwen-image",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Qwen-Image",
    ),
    # Replicate image generation
    Model(
        id="black-forest-labs/flux-krea-dev",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_GENERATION | Capability.IMAGE_EDIT,
        display_name="FLUX Krea Dev",
    ),
    # Video generation (Replicate)
    Model(
        id="bytedance/seedance-1-lite",
        provider=Provider.REPLICATE,
        capabilities=Capability.VIDEO_GENERATION,
        display_name="Seedance 1 Lite",
    ),
    # Video generation (Google)
    Model(
        id="veo-3.0-generate-preview",
        provider=Provider.GOOGLE,
        capabilities=Capability.VIDEO_GENERATION,
        display_name="Veo 3.0 Preview",
    ),
    Model(
        id="veo-3.0-fast-generate-preview",
        provider=Provider.GOOGLE,
        capabilities=Capability.VIDEO_GENERATION,
        display_name="Veo 3.0 Fast Preview",
    ),
    Model(
        id="veo-2.0-generate-001",
        provider=Provider.GOOGLE,
        capabilities=Capability.VIDEO_GENERATION,
        display_name="Veo 2.0",
    ),
    # Replicate Image Generation Models
    Model(
        id="stability-ai/sdxl",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Stable Diffusion XL",
    ),
    # Replicate Image Edit Models
    Model(
        id="qwen/qwen-image-edit",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_EDIT,
        display_name="Qwen Image Edit",
    ),
    Model(
        id="stability-ai/stable-diffusion",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="Stable Diffusion",
    ),
    Model(
        id="black-forest-labs/flux-schnell",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="FLUX Schnell",
    ),
    Model(
        id="black-forest-labs/flux-dev",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="FLUX Dev",
    ),
    Model(
        id="black-forest-labs/flux-pro",
        provider=Provider.REPLICATE,
        capabilities=Capability.IMAGE_GENERATION,
        display_name="FLUX Pro",
    ),
    # Audio transcription
    Model(
        id="gpt-4o-transcribe",
        provider=Provider.OPENAI,
        capabilities=Capability.AUDIO_TRANSCRIPTION,
        display_name="GPT-4o Transcribe",
    ),
    Model(
        id="gpt-4o-mini-transcribe",
        provider=Provider.OPENAI,
        capabilities=Capability.AUDIO_TRANSCRIPTION,
        display_name="GPT-4o Mini Transcribe",
    ),
    # Chat/text models (client)
    Model(
        id="o3-2025-04-16",
        provider=Provider.OPENAI,
        capabilities=Capability.TEXT_GENERATION | Capability.STRUCTURED_OUTPUT,
        display_name="o3",
    ),
    Model(
        id="o4-mini-2025-04-16",
        provider=Provider.OPENAI,
        capabilities=Capability.TEXT_GENERATION | Capability.STRUCTURED_OUTPUT,
        display_name="o4-mini",
    ),
    Model(
        id="gpt-4.1-2025-04-14",
        provider=Provider.OPENAI,
        capabilities=Capability.TEXT_GENERATION | Capability.STRUCTURED_OUTPUT,
        display_name="GPT-4.1",
    ),
    Model(
        id="gpt-5",
        provider=Provider.OPENAI,
        capabilities=Capability.TEXT_GENERATION | Capability.STRUCTURED_OUTPUT,
        display_name="GPT-5",
    ),
    Model(
        id="mistral-small-latest",
        provider=Provider.MISTRAL,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Mistral Small",
    ),
    Model(
        id="mistral-medium-latest",
        provider=Provider.MISTRAL,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Mistral Medium",
    ),
    Model(
        id="mistral-large-latest",
        provider=Provider.MISTRAL,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Mistral Large",
    ),
    Model(
        id="codestral-latest",
        provider=Provider.MISTRAL,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Codestral",
    ),
    Model(
        id="claude-3-7-sonnet-20250219",
        provider=Provider.ANTHROPIC,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Sonnet 3.7",
    ),
    Model(
        id="claude-sonnet-4-20250514",
        provider=Provider.ANTHROPIC,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Sonnet 4",
    ),
    Model(
        id="claude-opus-4-20250514",
        provider=Provider.ANTHROPIC,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Opus 4",
    ),
    Model(
        id="claude-opus-4-1-20250805",
        provider=Provider.ANTHROPIC,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Opus 4.1",
    ),
    Model(
        id="google/gemma-2-2b-it",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Gemma 2 2B (IT)",
    ),
    Model(
        id="meta-llama/Meta-Llama-3.1-8B-Instruct",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Llama 3.1 8B Instruct",
    ),
    Model(
        id="microsoft/phi-4",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Phi-4 (HF)",
    ),
    Model(
        id="Qwen/Qwen2.5-7B-Instruct-1M",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Qwen2.5 7B Instruct 1M",
    ),
    Model(
        id="Qwen/Qwen2.5-Coder-32B-Instruct",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Qwen2.5 Coder 32B Instruct",
    ),
    Model(
        id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="DeepSeek R1 Distill Qwen 1.5B",
    ),
    Model(
        id="deepseek-ai/DeepSeek-R1",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="DeepSeek R1",
    ),
    Model(
        id="Qwen/Qwen3-0.6B",
        provider=Provider.TRANSFORMERS,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Qwen3 0.6B",
    ),
    Model(
        id="openai-community/gpt2",
        provider=Provider.TRANSFORMERS,
        capabilities=Capability.TEXT_GENERATION,
        display_name="GPT-2",
    ),
    Model(
        id="HuggingFaceTB/SmolLM2-135M-Instruct",
        provider=Provider.TRANSFORMERS,
        capabilities=Capability.TEXT_GENERATION,
        display_name="SmolLM2 135M Instruct",
    ),
    Model(
        id="moonshotai/Kimi-K2-Instruct",
        provider=Provider.HUGGINGFACE,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Kimi K2 Instruct",
    ),
    Model(
        id="hf.co/mistralai/Magistral-Small-2506_gguf:Q8_0",
        provider=Provider.OLLAMA,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Magistral Small Q8_0",
    ),
    Model(
        id="llama3.2:latest",
        provider=Provider.OLLAMA,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Llama 3.2",
    ),
    Model(
        id="granite3.2:latest",
        provider=Provider.OLLAMA,
        capabilities=Capability.TEXT_GENERATION,
        display_name="Granite 3.2",
    ),
    Model(
        id="gpt-oss:20b",
        provider=Provider.OLLAMA,
        capabilities=Capability.TEXT_GENERATION,
        display_name="GPT OSS 20B (Ollama)",
    ),
    # Cohere reranking models
    Model(
        id="rerank-multilingual-v3.0",
        provider=Provider.COHERE,
        capabilities=Capability.RERANKING,
        display_name="Rerank Multilingual v3.0",
    ),
    Model(
        id="rerank-english-v3.0",
        provider=Provider.COHERE,
        capabilities=Capability.RERANKING,
        display_name="Rerank English v3.0",
    ),
    Model(
        id="rerank-multilingual-v2.0",
        provider=Provider.COHERE,
        capabilities=Capability.RERANKING,
        display_name="Rerank Multilingual v2.0",
    ),
    Model(
        id="rerank-english-v2.0",
        provider=Provider.COHERE,
        capabilities=Capability.RERANKING,
        display_name="Rerank English v2.0",
    ),
]


__all__ = ["CATALOG"]
