from typing import List, Self

from src.models.choice import Choice


class StateException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class State:
    def __init__(
        self: Self,
        current_mp: int,
        collection_limit: int,
        capacity_limit: int,
        collected_mp: int = 0,
        path: List[Choice] = [],
    ) -> None:
        self._current_mp: int = current_mp
        self._collected_mp: int = collected_mp
        self._collection_limit: int = collection_limit
        self._capacity_limit: int = capacity_limit
        self._path: List[Choice] = path

    @property
    def current_mp(self) -> int:
        return self._current_mp

    @property
    def collected_mp(self) -> int:
        return self._collected_mp

    @property
    def collection_limit(self) -> int:
        return self._collection_limit

    @property
    def capacity_limit(self) -> int:
        return self._capacity_limit

    @property
    def path(self) -> List[Choice]:
        return self._path

    def reached_collection_limit(self: Self) -> bool:
        return self._collected_mp >= self._collection_limit

    def reached_capacity_limit(self: Self) -> bool:
        return self._current_mp >= self._capacity_limit

    def valid(self: Self):
        return self._current_mp >= 0

    def can_collect_mp(self: Self) -> bool:
        return not any([self.reached_collection_limit(), self.reached_capacity_limit()])

    def next(self: Self, choice: Choice):
        is_power_spot = choice.cost > 0
        can_battle = self._current_mp >= choice.cost
        match (is_power_spot, can_battle, self.can_collect_mp()):
            case (True, True, True):
                """
                Battle & collect
                """
                return State(
                    current_mp=self._current_mp - choice.cost + choice.reward,
                    collected_mp=self._collected_mp + choice.reward,
                    collection_limit=self._collection_limit,
                    capacity_limit=self._capacity_limit,
                    path=self._path + [choice],
                )
            case (True, True, False):
                """
                Battle only
                """
                return State(
                    current_mp=self._current_mp - choice.cost,
                    collected_mp=self._collected_mp,
                    collection_limit=self._collection_limit,
                    capacity_limit=self._capacity_limit,
                    path=self._path + [Choice(cost=choice.cost)],
                )
            case (True, False, True):
                """
                Collect from power spot
                """
                return State(
                    current_mp=self._current_mp + choice.reward,
                    collected_mp=self._collected_mp + choice.reward,
                    collection_limit=self._collection_limit,
                    capacity_limit=self._capacity_limit,
                    path=self._path + [Choice(reward=choice.reward)],
                )
            case (False, _, True):
                """
                Collect from exploration
                """
                return State(
                    current_mp=self._current_mp + choice.reward,
                    collected_mp=self._collected_mp + choice.reward,
                    collection_limit=self._collection_limit,
                    capacity_limit=self._capacity_limit,
                    path=self._path + [choice],
                )
            case s:
                raise StateException("Next state is invalid")

    def __str__(self) -> str:
        return (
            "State:\n"
            + "\tMp: "
            + str(self._current_mp)
            + "\n"
            + "\tCollected: "
            + str(self._collected_mp)
            + "\n"
            + "\tCapacity: "
            + str(self._capacity_limit)
            + "\n"
            + "\tCollection limit: "
            + str(self._collection_limit)
            + "\n"
            + "\n".join(
                map(
                    lambda choice: "\t"
                    + "Choice: "
                    + "\n\t\t"
                    + "Cost: "
                    + str(choice.cost)
                    + "\n\t\t"
                    + "Reward: "
                    + str(choice.reward),
                    self._path,
                )
            )
        )
