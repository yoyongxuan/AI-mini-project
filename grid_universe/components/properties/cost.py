from dataclasses import dataclass


@dataclass(frozen=True)
class Cost:
    """
    Marker component for entities that impose a cost.

    Attributes:
        amount: Positive integer cost.
    """

    amount: int
