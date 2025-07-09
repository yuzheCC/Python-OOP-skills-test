from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List


class EventSource(ABC):
    """Abstract event source."""

    @abstractmethod
    def get_events(self) -> List[Dict[str, Any]]:  # noqa: D401
        """Return a list of event dictionaries ready for processing."""
        raise NotImplementedError


class RealTimeEventSource(EventSource):
    """Event source backed by an in-memory list."""

    def __init__(self, events: List[Dict[str, Any]]) -> None:
        self._events = events

    def get_events(self) -> List[Dict[str, Any]]:
        return list(self._events)


class ScheduledQueryEventSource(EventSource):
    """Event source that executes a query function (e.g., simulating SQL)."""

    def __init__(self, query_fn: Callable[..., List[Dict[str, Any]]], **params: Any) -> None:
        self._query_fn = query_fn
        self._params = params

    def get_events(self) -> List[Dict[str, Any]]:
        return self._query_fn(**self._params) 