from typing import List

from brick_processor import BrickProcessor


def read_input(file_path: str) -> List[str]:
    with open(file_path) as file:
        lines = file.readlines()
        
    return lines


def main() -> None:
    data = read_input('day_22/input.txt')
    
    total_stable_bricks, total_fallen_bricks = BrickProcessor(data).calculate_total_bricks()
    
    print(total_stable_bricks)
    print(total_fallen_bricks)


if __name__ == '__main__':
    main()