from __future__ import annotations

import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load .env exactly once, at import time
load_dotenv()


class OpenAISettings(BaseModel):
    api_key: str | None = Field(default_factory=lambda: os.getenv("OPENAI_API_KEY"), alias="OPENAI_API_KEY")


class GoogleSettings(BaseModel):
    api_key: str | None = Field(default_factory=lambda: os.getenv("GOOGLE_API_KEY"), alias="GOOGLE_API_KEY")


class AnthropicSettings(BaseModel):
    api_key: str | None = Field(
        default_factory=lambda: os.getenv("ANTHROPIC_API_KEY"),
        alias="ANTHROPIC_API_KEY",
    )


class MistralSettings(BaseModel):
    api_key: str | None = Field(default_factory=lambda: os.getenv("MISTRAL_API_KEY"), alias="MISTRAL_API_KEY")


class HuggingFaceSettings(BaseModel):
    access_token: str | None = Field(
        default_factory=lambda: os.getenv("HUGGINGFACE_TOKEN"),
        alias="HUGGINGFACE_TOKEN",
    )


class OllamaSettings(BaseModel):
    host: str | None = Field(
        default_factory=lambda: os.getenv("OLLAMA_HOST", "http://localhost:11434"),
        alias="OLLAMA_HOST",
    )


class StabilitySettings(BaseModel):
    api_key: str | None = Field(
        default_factory=lambda: os.getenv("STABILITYAI_API_KEY"),
        alias="STABILITYAI_API_KEY",
    )


class LumaSettings(BaseModel):
    api_key: str | None = Field(default_factory=lambda: os.getenv("LUMA_API_KEY"), alias="LUMA_API_KEY")


class XAISettings(BaseModel):
    api_key: str | None = Field(default_factory=lambda: os.getenv("XAI_API_KEY"), alias="XAI_API_KEY")


class ReplicateSettings(BaseModel):
    api_token: str | None = Field(
        default_factory=lambda: os.getenv("REPLICATE_API_TOKEN"),
        alias="REPLICATE_API_TOKEN",
    )


class CohereSettings(BaseModel):
    api_key: str | None = Field(default_factory=lambda: os.getenv("COHERE_API_KEY"), alias="COHERE_API_KEY")


class TopazLabsSettings(BaseModel):
    api_key: str | None = Field(
        default_factory=lambda: os.getenv("TOPAZLABS_API_KEY"),
        alias="TOPAZLABS_API_KEY",
    )


class CelesteSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
        env_nested_delimiter="__",
        extra="ignore",
    )
    openai: OpenAISettings = Field(default_factory=OpenAISettings)
    google: GoogleSettings = Field(default_factory=GoogleSettings)
    anthropic: AnthropicSettings = Field(default_factory=AnthropicSettings)
    mistral: MistralSettings = Field(default_factory=MistralSettings)
    huggingface: HuggingFaceSettings = Field(default_factory=HuggingFaceSettings)
    ollama: OllamaSettings = Field(default_factory=OllamaSettings)
    stability: StabilitySettings = Field(default_factory=StabilitySettings)
    luma: LumaSettings = Field(default_factory=LumaSettings)
    xai: XAISettings = Field(default_factory=XAISettings)
    replicate: ReplicateSettings = Field(default_factory=ReplicateSettings)
    cohere: CohereSettings = Field(default_factory=CohereSettings)
    topazlabs: TopazLabsSettings = Field(default_factory=TopazLabsSettings)

    # Pydantic v2 SettingsConfigDict above replaces old Config

    def _get_credential_for_provider(self, provider: str) -> tuple[str | None, str]:
        """Get credential value and env var name for a provider."""
        provider_map = {
            "openai": (self.openai.api_key, "OPENAI_API_KEY"),
            "anthropic": (self.anthropic.api_key, "ANTHROPIC_API_KEY"),
            "mistral": (self.mistral.api_key, "MISTRAL_API_KEY"),
            "google": (self.google.api_key, "GOOGLE_API_KEY"),
            "huggingface": (self.huggingface.access_token, "HUGGINGFACE_TOKEN"),
            "stabilityai": (self.stability.api_key, "STABILITYAI_API_KEY"),
            "luma": (self.luma.api_key, "LUMA_API_KEY"),
            "xai": (self.xai.api_key, "XAI_API_KEY"),
            "replicate": (self.replicate.api_token, "REPLICATE_API_TOKEN"),
            "cohere": (self.cohere.api_key, "COHERE_API_KEY"),
            "topazlabs": (self.topazlabs.api_key, "TOPAZLABS_API_KEY"),
        }
        return provider_map.get(provider.lower(), (None, ""))

    def validate_for_provider(self, provider: str) -> None:
        """
        Validate that required credentials are present for the selected provider.
        Raises ValueError with a helpful message when missing.
        """
        credential, env_var = self._get_credential_for_provider(provider)
        if env_var and not credential:
            raise ValueError(f"Missing required environment variable for provider '{provider}': {env_var}")

    def dump_masked(self) -> dict:
        def mask(value: str | None) -> str | None:
            if not value:
                return value
            return value[:3] + "***" if len(value) > 3 else "***"

        return {
            "openai": {"api_key": mask(self.openai.api_key)},
            "google": {"api_key": mask(self.google.api_key)},
            "anthropic": {"api_key": mask(self.anthropic.api_key)},
            "mistral": {"api_key": mask(self.mistral.api_key)},
            "huggingface": {"access_token": mask(self.huggingface.access_token)},
            "ollama": {"host": self.ollama.host},
            "stability": {"api_key": mask(self.stability.api_key)},
            "luma": {"api_key": mask(self.luma.api_key)},
            "xai": {"api_key": mask(self.xai.api_key)},
            "replicate": {"api_token": mask(self.replicate.api_token)},
            "cohere": {"api_key": mask(self.cohere.api_key)},
            "topazlabs": {"api_key": mask(self.topazlabs.api_key)},
        }


# Singleton-style accessor
settings = CelesteSettings()
