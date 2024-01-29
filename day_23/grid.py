from typing import List, Tuple, Dict, Set


class Grid:
    def __init__(self, data: List[str]):
        self.data = data
        self.num_rows = len(data)
        self.num_columns = len(data[0])
        self.ground_map = self.parse_map(data)
        self.splits = self.separate_splits()

    @staticmethod
    def parse_map(data: List[str]) -> Dict[Tuple[int, int], str]:
        ground_map = dict()

        for row_index, row in enumerate(data):
            for column_index, tile in enumerate(row):
                ground_map[row_index, column_index] = tile

        return ground_map

    def is_valid_tile(self, row: int, column: int) -> bool:
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        directions = [UP, DOWN, LEFT, RIGHT]
        count = sum(self.ground_map[row + delta_row, column + delta_column] == '#' for (delta_row, delta_column) in directions)

        return self.ground_map[row, column] == '.' and count < 2

    def separate_splits(self) -> Set[Tuple[int, int]]:
        splits = set()

        for row in range(1, self.num_rows - 1):
            for column in range(1, self.num_columns - 1):
                if self.is_valid_tile(row, column):
                    splits.add((row, column))

        splits.add((0, 1))
        splits.add((self.num_rows - 1, self.num_columns - 2))

        return splits