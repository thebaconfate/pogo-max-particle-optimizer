from typing import Self

from src.models.state import State


class Choice:
    def __init__(self, name, cost=0, gain=0, collect_gain=0, battles=0):
        self.name = name
        self.cost = cost  # battle cost
        self.gain = gain  # flat points gain (explore, collect)
        self.collect_gain = collect_gain
        self.battles = battles

    def apply(self, state: State):
        """Return a new state after applying this choice."""
        new_points = state.points + self.gain - self.cost
        new_collected = state.collected + self.collect_gain
        new_can_collect = state.can_collect

        # If we crossed the limit → no more collecting allowed
        if new_collected > state.collection_limit or new_points > state.capacity_limit:
            new_can_collect = False

        if new_points < 0:
            return None  # invalid (not enough points)
        return State(
            points=new_points,
            collected=new_collected,
            collection_limit=state.collection_limit,
            capacity_limit=state.capacity_limit,
            can_collect=new_can_collect,
        )
