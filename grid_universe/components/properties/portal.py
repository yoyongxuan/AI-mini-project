from dataclasses import dataclass


@dataclass(frozen=True)
class Portal:
    """
    Portal property component.

    Attributes:
        pair_entity: Entity ID of the paired portal.
    """

    pair_entity: int
