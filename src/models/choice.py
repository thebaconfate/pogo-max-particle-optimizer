from typing import Self


class Choice:
    def __init__(self: Self, cost: int = 0, reward: int = 0) -> None:
        self._cost = cost
        self._reward = reward
        if self._reward == 0 and self._cost == 0:
            raise ValueError("cost and reward cannot be 0 simultaneously")
        if self._reward < 0 or self._cost < 0:
            raise ValueError("cost and reward cannot be negative")

    @property
    def cost(self: Self) -> int:
        return self._cost

    @property
    def reward(self: Self) -> int:
        return self._reward

    def __str__(self) -> str:
        return (
            "Choice:"
            + "\n"
            + "\n".join(
                map(
                    lambda x: "\t" + str(x),
                    [f"Cost: {self._cost}", f"Reward: {self._reward}"],
                )
            )
        )
