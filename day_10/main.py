from typing import List

from pipe_maze_solver import PipeMazeSolver


def read_file(file_path) -> List[str]:
    with open(file_path) as file:
        content = file.read().split()

    return content


def main():
    sketch = read_file('day_10/input.txt')

    solver = PipeMazeSolver(sketch)
    distance = solver.bfs()
    inside_loop = solver.count_tiles_inside_loop()

    print(distance)
    print(inside_loop)


if __name__ == '__main__':
    main()
