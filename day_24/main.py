import itertools
from typing import List, Tuple

from hailstone import Hailstone, Position
from hailstone_position_finder import HailstonePositionFinder
from collision_checker import CollisionChecker


def read_file(file_path: str) -> List[str]:
    with open(file_path) as file:
        content = file.readlines()

    return content


def parse_hailstones(data: List[str]) -> List[Tuple[Position, Position]]:
    hailstones = []
    
    for hailstone in data:
        position, velocity = hailstone.split(" @ ")
        positions = list(map(int, position.split(", ")))
        velocities = list(map(int, velocity.split(", ")))
        hailstones.append(Hailstone(Position(*positions), Position(*velocities)))
    
    return hailstones


def main() -> None:
    data = read_file('day_24/input.txt')
    hailstones = parse_hailstones(data)

    collision_checker = CollisionChecker()
    
    collision_count = 0
    for first_hailstone, second_hailstone in itertools.combinations(hailstones, 2):
        if collision_checker.check_collision(first_hailstone, second_hailstone):
            collision_count += 1

    stone_position = HailstonePositionFinder().find_stone_position(hailstones)

    print(collision_count)
    print(sum(stone_position))


if __name__ == '__main__':
    main()
