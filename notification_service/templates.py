from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from jinja2 import Environment

_env = Environment(autoescape=False)


@dataclass(frozen=True, slots=True)
class Template:
    """Thin wrapper around a Jinja2 template string."""

    name: str
    text: str

    def render(self, data: Dict[str, Any]) -> str:
        template = _env.from_string(self.text)
        return template.render(**data) 