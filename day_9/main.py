from oasis import Oasis


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.readlines()

    return content


def main() -> None:
    data = read_file('day_9/input.txt')

    oasis = Oasis(data)
    sum_future_extrapolated_values = oasis.calculate_sum_future_extrapolated_values()
    sum_past_extrapolated_values = oasis.calculate_sum_past_extrapolated_values()

    print(sum_future_extrapolated_values)
    print(sum_past_extrapolated_values)


if __name__ == '__main__':
    main()
