from dataclasses import dataclass


@dataclass(frozen=True)
class Locked:
    """
    Locked property component.

    Attributes:
        key_id: Identifier string used to unlock this entity. If empty, may mean
                "locked with no key" or generic lock.
    """

    key_id: str = ""  # If empty, may mean "locked with no key" or generic lock
