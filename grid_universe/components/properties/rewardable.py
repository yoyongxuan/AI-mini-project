from dataclasses import dataclass


@dataclass(frozen=True)
class Rewardable:
    """
    Marker component for rewardable entities.

    Attributes:
        amount: The reward amount granted upon interaction.
    """

    amount: int
