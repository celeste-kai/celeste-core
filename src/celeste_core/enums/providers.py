from enum import Enum


class Provider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    MISTRAL = "mistral"
    GOOGLE = "google"
    LOCAL = "local"
    HUGGINGFACE = "huggingface"
    TRANSFORMERS = "transformers"
    OLLAMA = "ollama"
    STABILITYAI = "stabilityai"
    LUMA = "luma"
    XAI = "xai"
    REPLICATE = "replicate"
    COHERE = "cohere"
    TOPAZLABS = "topazlabs"
