from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, Dict
import uuid


class NotificationChannel(ABC):
    """Abstract base class for all notification channels."""

    @abstractmethod
    def send(self, message: str, metadata: Dict[str, Any] | None = None) -> None:  # noqa: D401
        """Send a message via the channel."""
        raise NotImplementedError


class EmailChannel(NotificationChannel):
    """Mock email channel that writes messages to files in an 'outbox' directory."""

    def __init__(self, outbox_dir: str | Path = "outbox") -> None:
        self.outbox_dir = Path(outbox_dir)
        self.outbox_dir.mkdir(parents=True, exist_ok=True)

    def send(self, message: str, metadata: Dict[str, Any] | None = None) -> None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"email_{timestamp}_{uuid.uuid4().hex[:8]}.txt"
        filepath = self.outbox_dir / filename
        with open(filepath, "w", encoding="utf-8") as fp:
            fp.write(message)
        print(f"[EmailChannel] Wrote email to {filepath.absolute()}")


class SlackChannel(NotificationChannel):
    """Mock Slack channel that prints messages to the console."""

    def send(self, message: str, metadata: Dict[str, Any] | None = None) -> None:  # noqa: D401
        channel = metadata.get("slack_channel", "#general") if metadata else "#general"
        print(f"[SlackChannel] Posting to {channel}: {message}") 
