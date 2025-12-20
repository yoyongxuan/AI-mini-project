"""
Terminal state utilities.

Provides helper functions to determine if the current state is terminal
(win/loss) or valid (agent exists and has a position).
"""

from grid_universe.state import State
from grid_universe.types import EntityID


def is_valid_state(state: State, agent_id: EntityID) -> bool:
    """Return True if agent exists and has a position."""
    return len(state.agent) > 0 and state.position.get(agent_id) is not None


def is_terminal_state(state: State, agent_id: EntityID) -> bool:
    """Return True if state already satisfies win/lose or agent is dead."""
    return state.win or state.lose or agent_id in state.dead
