from dataclasses import dataclass


@dataclass(frozen=True)
class Required:
    """
    Marker component for required entities.
    """

    pass
