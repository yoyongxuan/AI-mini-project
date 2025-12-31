from collections.abc import Hashable
from typing import TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V", bound=Hashable)


class HashableDict(dict[K, V]):
    """A hashable dictionary implementation (dangerous if mutated after hashing)."""

    def __hash__(self) -> int:  # type: ignore[override]
        return hash(frozenset(self.items()))
