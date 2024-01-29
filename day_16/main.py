from energized_tiles_counter import EnergizedTilesCounter


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def main() -> None:
    contraption_data = read_file('day_16/input.txt')

    energized_tiles_counter = EnergizedTilesCounter(contraption_data)

    energized_tiles = energized_tiles_counter.count_energized_tiles((0, 0), (0, 1))
    print(energized_tiles)

    max_energized_tiles = energized_tiles_counter.find_max_energized_tiles()
    print(max_energized_tiles)


if __name__ == '__main__':
    main()