from dataclasses import dataclass


@dataclass(frozen=True)
class Collidable:
    """
    Marker component for collidable entities (e.g., portal entry).
    """

    pass
