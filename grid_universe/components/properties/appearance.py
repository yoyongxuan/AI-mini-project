from dataclasses import dataclass
from enum import StrEnum, auto


class AppearanceName(StrEnum):
    """Enumeration of built‑in appearance names."""

    NONE = auto()
    BOOTS = auto()
    BOX = auto()
    COIN = auto()
    CORE = auto()
    DOOR = auto()
    EXIT = auto()
    FLOOR = auto()
    GEM = auto()
    GHOST = auto()
    HUMAN = auto()
    KEY = auto()
    LAVA = auto()
    LOCK = auto()
    MONSTER = auto()
    PORTAL = auto()
    SHIELD = auto()
    SPIKE = auto()
    WALL = auto()


@dataclass(frozen=True)
class Appearance:
    """
    Rendering appearance properties.

    Attributes:
        name: Appearance name.
        priority: Integer priority used for layering selection.
        icon: If True this entity may render as a small corner icon.
        background: If True this entity may render as a background tile.
    """

    name: AppearanceName
    priority: int = 0
    icon: bool = False
    background: bool = False
