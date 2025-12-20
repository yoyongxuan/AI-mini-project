from dataclasses import dataclass


@dataclass(frozen=True)
class Dead:
    """
    Marker component for dead entities.
    """

    pass
