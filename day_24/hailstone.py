from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int
    z: int


class Hailstone:
    def __init__(self, initial_position: Position, initial_velocity: Position):
        self.position = initial_position
        self.velocity = initial_velocity