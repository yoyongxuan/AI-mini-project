from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Optional

from grid_universe.components.properties.position import Position


class MovingAxis(StrEnum):
    """
    Axis of autonomous movement.
    """

    HORIZONTAL = auto()
    VERTICAL = auto()


@dataclass(frozen=True)
class Moving:
    """
    Autonomous movement component.

    Attributes:
        axis: Axis of autonomous movement (horizontal or vertical).
        direction: +1 or -1 indicating step direction along the axis. +1 is right/down, -1 is left/up.
        bounce: Reverse direction upon hitting an obstacle if True; stop moving if False.
        speed: Number of steps to move per tick.
        prev_position: Internal tracking of previous position (set by system).
    """

    axis: MovingAxis
    direction: int  # 1 or -1
    bounce: bool = True
    speed: int = 1
    prev_position: Optional[Position] = None
