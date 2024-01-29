from scratch_card_calculator import ScratchCardCalculator


def main() -> None:
    with open('day_4/input.txt') as file:
        card_strings = file.readlines()

    calculator = ScratchCardCalculator()
    total_points, total_copies = calculator.calculate_scratch_cards(card_strings)

    print(total_points)
    print(total_copies)


if __name__ == "__main__":
    main()
