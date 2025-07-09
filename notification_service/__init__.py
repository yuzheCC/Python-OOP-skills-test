"""
Notification Service package providing extensible pluggable notification framework.
"""

from .channels import EmailChannel, SlackChannel, NotificationChannel
from .templates import Template
from .events import RealTimeEventSource, ScheduledQueryEventSource
from .dedup import InMemoryDedupPolicy
from .notification import Notification
from .registry import NotificationRegistry

__all__: list[str] = [
    "NotificationChannel",
    "EmailChannel",
    "SlackChannel",
    "Template",
    "RealTimeEventSource",
    "ScheduledQueryEventSource",
    "InMemoryDedupPolicy",
    "Notification",
    "NotificationRegistry",
] 