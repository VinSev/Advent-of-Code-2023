from typing import List

from camel_cards_game import CamelCardsGame
from hand_strategy import Part1HandStrategy, Part2HandStrategy


def read_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        content = file.readlines()

    return content


def main() -> None:
    data = read_file('day_7/input.txt')

    orderer = CamelCardsGame(data, Part1HandStrategy())

    orderer.order_hands()
    score = orderer.calculate_score()
    print('Part 1:', score)
    
    orderer = CamelCardsGame(data, Part2HandStrategy())

    orderer.order_hands()
    score = orderer.calculate_score()
    print('Part 2:', score)


if __name__ == '__main__':
    main()
