from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from .channels import NotificationChannel
from .dedup import DedupPolicy, InMemoryDedupPolicy
from .events import EventSource
from .templates import Template


@dataclass
class Notification:
    """A single notification configuration (channel + template + source)."""

    name: str
    channel: NotificationChannel
    template: Template
    event_source: EventSource
    dedup_policy: DedupPolicy = field(default_factory=InMemoryDedupPolicy)

    def process(self) -> None:
        """Fetch events, render templates, and send messages via the configured channel."""
        for event in self.event_source.get_events():
            if self.dedup_policy and self.dedup_policy.is_duplicate(event):
                continue
            message = self.template.render(event)
            metadata: Dict[str, Any] = dict(event)  # pass event dict to channel
            self.channel.send(message, metadata) 