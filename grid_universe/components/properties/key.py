from dataclasses import dataclass


@dataclass(frozen=True)
class Key:
    """
    Key component.

    Attributes:
        key_id: Identifier string used to unlock matching locked entities.
    """

    key_id: str  # 'red', 'blue', etc.
