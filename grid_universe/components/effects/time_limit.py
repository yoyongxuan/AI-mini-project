from dataclasses import dataclass


@dataclass(frozen=True)
class TimeLimit:
    """
    An effect that lasts for a limited number of time steps.

    Attributes:
        amount: Number of time steps the effect remains active.
    """

    amount: int
