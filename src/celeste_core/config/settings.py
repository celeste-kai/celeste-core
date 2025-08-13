from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load .env exactly once, at import time
load_dotenv()


class OpenAISettings(BaseModel):
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY"), alias="OPENAI_API_KEY"
    )


class GoogleSettings(BaseModel):
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("GOOGLE_API_KEY"), alias="GOOGLE_API_KEY"
    )


class AnthropicSettings(BaseModel):
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("ANTHROPIC_API_KEY"),
        alias="ANTHROPIC_API_KEY",
    )


class MistralSettings(BaseModel):
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("MISTRAL_API_KEY"), alias="MISTRAL_API_KEY"
    )


class HuggingFaceSettings(BaseModel):
    access_token: Optional[str] = Field(
        default_factory=lambda: os.getenv("HUGGINGFACE_TOKEN"),
        alias="HUGGINGFACE_TOKEN",
    )


class OllamaSettings(BaseModel):
    host: Optional[str] = Field(
        default_factory=lambda: os.getenv("OLLAMA_HOST", "http://localhost:11434"),
        alias="OLLAMA_HOST",
    )


class StabilitySettings(BaseModel):
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("STABILITYAI_API_KEY"),
        alias="STABILITYAI_API_KEY",
    )


class LumaSettings(BaseModel):
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("LUMA_API_KEY"), alias="LUMA_API_KEY"
    )


class XAISettings(BaseModel):
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("XAI_API_KEY"), alias="XAI_API_KEY"
    )


class ReplicateSettings(BaseModel):
    api_token: Optional[str] = Field(
        default_factory=lambda: os.getenv("REPLICATE_API_TOKEN"),
        alias="REPLICATE_API_TOKEN",
    )


class CelesteSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
        env_nested_delimiter="__",
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

    # Pydantic v2 SettingsConfigDict above replaces old Config

    def validate_for_provider(self, provider: str) -> None:
        """
        Validate that required credentials are present for the selected provider.
        Raises ValueError with a helpful message when missing.
        """
        missing: list[str] = []
        p = provider.lower()
        if p == "openai" and not self.openai.api_key:
            missing.append("OPENAI_API_KEY")
        if p == "anthropic" and not self.anthropic.api_key:
            missing.append("ANTHROPIC_API_KEY")
        if p == "mistral" and not self.mistral.api_key:
            missing.append("MISTRAL_API_KEY")
        if p == "google" and not self.google.api_key:
            missing.append("GOOGLE_API_KEY")
        if p == "huggingface" and not self.huggingface.access_token:
            missing.append("HUGGINGFACE_TOKEN")
        if p == "stabilityai" and not self.stability.api_key:
            missing.append("STABILITYAI_API_KEY")
        if p == "luma" and not self.luma.api_key:
            missing.append("LUMA_API_KEY")
        if p == "xai" and not self.xai.api_key:
            missing.append("XAI_API_KEY")
        if p == "replicate" and not self.replicate.api_token:
            missing.append("REPLICATE_API_TOKEN")

        if missing:
            raise ValueError(
                f"Missing required environment variables for provider "
                f"'{provider}': {', '.join(missing)}"
            )

    def dump_masked(self) -> dict:
        def mask(value: Optional[str]) -> Optional[str]:
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
        }


# Singleton-style accessor
settings = CelesteSettings()
