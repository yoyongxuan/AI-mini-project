from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """
    Grid position component.

    Attributes:
        x: X-coordinate on the grid.
        y: Y-coordinate on the grid.
    """

    x: int
    y: int
