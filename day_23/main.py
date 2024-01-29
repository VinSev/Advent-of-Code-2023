from typing import List

from grid import Grid
from pathfinder import Pathfinder


def read_file(file_path: str) -> List[str]:
    with open(file_path) as file:
        content = file.read().split('\n')
        
    return content

    
def main() -> None:
    data = read_file('day_23/input.txt')

    grid = Grid(data)
    pathfinder = Pathfinder(grid)

    max_steps_for_hike = pathfinder.find_max_steps(use_reverse=False)
    print(max_steps_for_hike)

    max_steps_for_hike = pathfinder.find_max_steps(use_reverse=True)
    print(max_steps_for_hike)


if __name__ == '__main__':
    main()
