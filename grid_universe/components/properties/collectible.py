from dataclasses import dataclass


@dataclass(frozen=True)
class Collectible:
    """
    Marker component for collectible entities (e.g., items that can be picked up).
    If combined with rewardable, collecting the entity grants a reward.
    If combined with required, collecting the entity is a requirement for level completion if the objective of the level includes collecting required items.
    """

    pass
