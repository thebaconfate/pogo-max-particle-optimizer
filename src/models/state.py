from typing import Any, Self


class StateException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class State:
    def __init__(
        self, points, collection_limit, capacity_limit, collected=0, can_collect=True
    ):
        self.points = points
        self.collected = collected
        self.can_collect = can_collect
        self.collection_limit = collection_limit
        self.capacity_limit = capacity_limit

    def __hash__(self: Self):
        return hash((self.points, self.collected, self.can_collect))

    def __eq__(self: Self, other: Any):
        return (
            self.points,
            self.collected,
            self.collection_limit,
            self.capacity_limit,
            self.can_collect,
        ) == (
            other.points,
            other.collected,
            other.collection_limit,
            other.capacity_limit,
            other.can_collect,
        )
