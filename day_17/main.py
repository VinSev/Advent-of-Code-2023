from pathfinder import Pathfinder


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def main() -> None:
    board_data = read_file('day_17/input.txt')

    min_moves, max_moves = 1, 3
    pathfinder = Pathfinder(board_data, min_moves, max_moves)
    print(pathfinder.calculate_minimal_heat())

    min_moves, max_moves = 4, 10
    pathfinder = Pathfinder(board_data, min_moves, max_moves)
    print(pathfinder.calculate_minimal_heat())


if __name__ == "__main__":
    main()
