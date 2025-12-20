from dataclasses import dataclass


@dataclass(frozen=True)
class UsageLimit:
    """
    An effect that can be used a limited number of times.

    Attributes:
        amount: Number of uses remaining.
    """

    amount: int
