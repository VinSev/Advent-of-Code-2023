from collections import deque
from typing import List, Set, Tuple

from movement_handler import MovementHandler


class EnergizedTilesCounter:
    def __init__(self, contraption_data: str) -> None:
        self.contraption = self.parse_contraption(contraption_data)
        self.num_rows = len(self.contraption)
        self.num_cols = len(self.contraption[0])
        self.visited_tiles: Set[Tuple[int, int, int, int]] = set()
        self.queue: deque = deque()

    @staticmethod
    def parse_contraption(contraption_data: str) -> List[str]:
        return contraption_data.split('\n')

    def update_visited_tiles(self, row: int, column: int, delta_row: int, delta_column: int) -> None:
        self.visited_tiles.add((row, column, delta_row, delta_column))

    def handle_cell_movement(self, cell: str, row: int, column: int, delta_row: int, delta_column: int) -> Tuple[int, int]:
        return MovementHandler(cell, row, column).handle_movement(self.queue, delta_row, delta_column)
    
    def is_valid_tile(self, row: int, column: int, delta_row: int, delta_column: int) -> bool:
        return 0 <= row < self.num_rows and 0 <= column < self.num_cols and (row, column, delta_row, delta_column) not in self.visited_tiles

    def process_tile(self, row: int, column: int, delta_row: int, delta_column: int) -> None:
        while self.is_valid_tile(row, column, delta_row, delta_column):
            self.update_visited_tiles(row, column, delta_row, delta_column)

            cell = self.contraption[row][column]

            delta_row, delta_column = self.handle_cell_movement(cell, row, column, delta_row, delta_column)

            row += delta_row
            column += delta_column

    def count_energized_tiles(self, position: Tuple[int, int], direction: Tuple[int, int]) -> int:
        self.queue.append((*position, *direction))

        while self.queue:
            row, column, delta_row, delta_column = self.queue.pop()
            self.process_tile(row, column, delta_row, delta_column)

        return len(set((row, column) for row, column, *_ in self.visited_tiles))

    def update_max_energized_tiles(self, start_pos: Tuple[int, int], direction: Tuple[int, int], max_energized_tiles: int) -> int:
        self.visited_tiles.clear()

        return max(max_energized_tiles, self.count_energized_tiles(start_pos, direction))

    def find_max_energized_tiles(self) -> int:
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

        max_energized_tiles = 0

        for row in range(self.num_rows):
            max_energized_tiles = self.update_max_energized_tiles(
                (row, self.num_cols - 1), LEFT, max_energized_tiles
            )
            max_energized_tiles = self.update_max_energized_tiles(
                (row, 0), RIGHT, max_energized_tiles
            )

        for column in range(self.num_cols):
            max_energized_tiles = self.update_max_energized_tiles(
                (self.num_rows - 1, column), UP, max_energized_tiles
            )
            max_energized_tiles = self.update_max_energized_tiles(
                (0, column), DOWN, max_energized_tiles
            )

        return max_energized_tiles