import sys
from pathlib import Path
from typing import Any

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from celeste_core.config.settings import CelesteSettings


def test_extra_env_fields_are_ignored(monkeypatch: Any) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "testkey")
    monkeypatch.setenv("CUSTOM_VAR", "hello")
    settings = CelesteSettings()
    assert settings.openai.api_key == "testkey"
    assert not hasattr(settings, "custom_var")
