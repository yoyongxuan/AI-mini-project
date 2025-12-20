from dataclasses import dataclass


@dataclass(frozen=True)
class Health:
    """
    Health component.

    Attributes:
        health: Current health points.
        max_health: Maximum health points.
    """

    health: int
    max_health: int
