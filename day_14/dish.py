from typing import List


class Dish:
    ROUND = 'O'
    CUBE = '#'
    EMPTY = '.'

    def __init__(self, data: str) -> None:
        self.grid = self.parse_grid(data)

    @staticmethod
    def parse_grid(data: str) -> List[List[str]]:
        return [list(row) for row in data.split('\n')]

    def rotate(self) -> None:
        self.grid = [list(row) for row in zip(*self.grid[::-1])]

    def roll(self) -> None:
        num_rows, num_cols = len(self.grid), len(self.grid[0])

        for column in range(num_cols):
            for _ in range(num_rows):
                self.update_grid_cells(column)

    def is_round_above_empty(self, row: int, col: int) -> bool:
        return self.grid[row][col] == self.ROUND and row > 0 and self.grid[row - 1][col] == self.EMPTY

    def update_grid_cells(self, col: int) -> None:
        num_rows = len(self.grid)

        for row in range(num_rows):
            if self.is_round_above_empty(row, col):
                self.grid[row][col] = self.EMPTY
                self.grid[row - 1][col] = self.ROUND

    def calculate_score(self) -> int:
        total_score = 0
        num_rows = len(self.grid)

        for row_index, row in enumerate(self.grid):
            total_score += (num_rows - row_index) * row.count(self.ROUND)

        return total_score