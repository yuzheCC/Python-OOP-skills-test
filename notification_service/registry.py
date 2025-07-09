from __future__ import annotations

from typing import List

from .notification import Notification


class NotificationRegistry:
    """Container for all notification configurations."""

    def __init__(self) -> None:
        self._notifications: List[Notification] = []

    def register(self, notification: Notification) -> None:
        self._notifications.append(notification)

    def list_all(self) -> List[Notification]:
        return list(self._notifications)

    def process_all(self) -> None:
        for notification in self._notifications:
            notification.process()

    def __str__(self) -> str:  # noqa: D401
        parts = ["Registered Notifications:"]
        for n in self._notifications:
            parts.append(
                f"- {n.name} | Channel={n.channel.__class__.__name__} | Template={n.template.name} | EventSource={n.event_source.__class__.__name__}"
            )
        return "\n".join(parts) 