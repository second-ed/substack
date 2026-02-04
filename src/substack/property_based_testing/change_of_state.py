from enum import Enum
from typing import Self


class State(Enum):
    OPEN = "open"
    CLOSED = "closed"


class Lock:
    def __init__(self) -> None:
        self.state = State.OPEN

    def lock(self) -> Self:
        if self.state == State.CLOSED:
            raise ValueError("Can't lock already locked")
        self.state = State.CLOSED
        return self

    def unlock(self) -> Self:
        if self.state == State.OPEN:
            raise ValueError("Can't unlock already unlocked")
        self.state = State.OPEN
        return self
