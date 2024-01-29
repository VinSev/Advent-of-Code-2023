from collections import defaultdict
from typing import Tuple, Dict, List


class CubeInventory:
    COLOR_LIMITS: Dict[str, int] = {'red': 12, 'green': 13, 'blue': 14}

    def __init__(self) -> None:
        self.sum_of_game_ids: int = 0
        self.sum_of_minimum_sets: int = 0

    def process_games(self, games: List[str]) -> None:
        for game in games:
            game_id, turns = game.split(':')
            cube_data, is_valid = self.process_turns(turns)

            if is_valid:
                self.sum_of_game_ids += int(game_id.split()[-1])

            # --- Added for Second Puzzle
            score = self.calculate_score(cube_data)
            self.sum_of_minimum_sets += score
            # ---

    def process_turns(self, turns: str) -> Tuple[defaultdict, bool]:
        cube_data = defaultdict(int)
        is_valid = True

        for turn in turns.split(';'):
            cube_data, is_valid = self.process_turn(turn, cube_data, is_valid)

        return cube_data, is_valid

    def process_turn(self, turn: str, cube_data: defaultdict, is_valid: bool) -> Tuple[defaultdict, bool]:
        for cube in turn.split(','):
            color_amount, color_name = cube.split()
            color_amount = int(color_amount)
            cube_data[color_name] = max(cube_data[color_name], color_amount)

            if color_amount > self.COLOR_LIMITS.get(color_name, 0):
                is_valid = False

        return cube_data, is_valid

    def calculate_score(self, cube_data: defaultdict) -> int:
        score = 1

        for color_amounts in cube_data.values():
            score *= color_amounts

        return score