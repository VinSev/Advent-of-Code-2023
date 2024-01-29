import math
from typing import List

from boat_race import BoatRace
from race_data_parser import PartOneParser, PartTwoParser


def read_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        content = file.readlines()

    return content


def main() -> None:
    data = read_file('day_6/input.txt')

    race_part_one = BoatRace(data, PartOneParser)
    amount_of_ways_to_win_list = race_part_one.calculate_ways_to_win()
    product_of_wins = math.prod(amount_of_ways_to_win_list)
    print(product_of_wins)

    race_part_two = BoatRace(data, PartTwoParser)
    amount_of_ways_to_win_list = race_part_two.calculate_ways_to_win()
    product_of_wins = math.prod(amount_of_ways_to_win_list)
    print(product_of_wins)


if __name__ == '__main__':
    main()
