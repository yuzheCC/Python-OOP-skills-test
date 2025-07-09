from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Set


class DedupPolicy(ABC):
    """Abstract base class for de-duplication policies."""

    @abstractmethod
    def is_duplicate(self, event: Dict[str, Any]) -> bool:  # noqa: D401
        """Return True if the event is a duplicate and should be skipped."""
        raise NotImplementedError


class InMemoryDedupPolicy(DedupPolicy):
    """Simple in-memory deduplication by tracking a single identifier field."""

    def __init__(self, id_field: str = "id") -> None:
        self.id_field = id_field
        self._seen: Set[Any] = set()

    def is_duplicate(self, event: Dict[str, Any]) -> bool:
        identifier = event.get(self.id_field)
        if identifier in self._seen:
            return True
        self._seen.add(identifier)
        return False 