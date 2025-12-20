from dataclasses import dataclass


@dataclass(frozen=True)
class Damage:
    """
    Marker component for damaging entities.

    Attributes:
        amount: Positive integer damage amount.
    """

    amount: int
