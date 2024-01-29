from steps_hash_sum_calculator import StepsHashSumCalculator
from steps_processor import StepsProcessor


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def main() -> None:
    data = read_file('day_15/input.txt')

    steps_processor = StepsProcessor(data)
    steps = steps_processor.steps

    hash_sum_calculator = StepsHashSumCalculator(steps)
    hash_sum = hash_sum_calculator.calculate_steps_hash_sum()
    print(hash_sum)

    steps_processor.process_steps()
    result = steps_processor.calculate_score()
    print(result)


if __name__ == '__main__':
    main()
