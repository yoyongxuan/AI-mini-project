from dataclasses import dataclass


@dataclass(frozen=True)
class Speed:
    """Movement multiplier.

    Attributes:
        multiplier: Positive integer multiplier.
    """

    multiplier: int
