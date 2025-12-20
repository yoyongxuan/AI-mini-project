from dataclasses import dataclass


@dataclass(frozen=True)
class Pushable:
    """
    Marker component for pushable entities (e.g., boxes).
    """

    pass
