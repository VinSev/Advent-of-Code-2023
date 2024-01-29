from dish_processor import DishProcessor


def read_input(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.read().strip()

    return content


def main() -> None:
    data = read_input('day_14/input.txt')

    num_target_cycles = 1
    num_rotations_per_cycle = 0

    dish_processor = DishProcessor(data, num_target_cycles, num_rotations_per_cycle)
    single_tilt_score = dish_processor.process_dish_cycles()
    print(single_tilt_score)

    num_target_cycles = 1_000_000_000
    num_rotations_per_cycle = 4

    dish_processor = DishProcessor(data, num_target_cycles, num_rotations_per_cycle)
    billion_cycle_score = dish_processor.process_dish_cycles()
    print(billion_cycle_score)


if __name__ == "__main__":
    main()