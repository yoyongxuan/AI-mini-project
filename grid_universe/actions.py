from enum import StrEnum, auto


class Action(StrEnum):
    """String enum of player actions.

    Enum Members:
        UP: Move up.
        DOWN: Move down.
        LEFT: Move left.
        RIGHT: Move right.
        USE_KEY: Attempt to unlock adjacent locked entities with a matching key.
        PICK_UP: Collect items (powerups / coins / cores / keys) at the current tile.
        WAIT: Advance a turn without doing anything.
    """

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    USE_KEY = auto()
    PICK_UP = auto()
    WAIT = auto()


MOVE_ACTIONS = [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]
