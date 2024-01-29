from almanac import Almanac


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.read().strip()

    return content


def main() -> None:
    data = read_file('day_5/input.txt')
    almanac = Almanac(data)

    locations = almanac.calculate_locations()
    print(min(locations))

    processed_ranges = almanac.calculate_ranges()
    print(min(processed_ranges))


if __name__ == '__main__':
    main()
