from galaxy_image import GalaxyImage


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def main() -> None:
    file_path = 'day_11/input.txt'
    data = read_file(file_path)

    galaxy_image = GalaxyImage(data, 2)
    total_distance_part_one = galaxy_image.calculate_sum_distances()

    galaxy_image = GalaxyImage(data, 1000000)
    total_distance_part_two = galaxy_image.calculate_sum_distances()

    print(total_distance_part_one)
    print(total_distance_part_two)


if __name__ == '__main__':
    main()
