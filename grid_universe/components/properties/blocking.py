from dataclasses import dataclass


@dataclass(frozen=True)
class Blocking:
    """
    Marker component for blocking entities (e.g., walls, obstacles).
    """

    pass
