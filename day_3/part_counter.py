from typing import List, Dict, Tuple, Set
from collections import defaultdict


class PartCounter:
    ADJACENT_OFFSETS: List[int] = [-1, 0, 1]

    def __init__(self, schematic_grid):
        self.schematic_grid = schematic_grid
        self.num_rows = len(schematic_grid)
        self.num_cols = len(schematic_grid[0])
        self.total_score = 0
        self.part_counts = defaultdict(list)

    def count_parts(self) -> Tuple[int, Dict[Tuple[int, int], List[int]]]:
        for row in range(self.num_rows):
            gears: Set[Tuple[int, int]] = set()
            number: int = 0

            for col in range(self.num_cols + 1):
                number, gears = self.count_part(row, col, number, gears)

        return self.total_score, self.part_counts

    def count_part(self, row: int, col: int, number: int, gears: Set[Tuple[int, int]]) -> Tuple[int, Set[Tuple[int, int]]]:
        if self.is_digit(row, col):
            self.process_gears(row, col, gears)
            number = number * 10 + int(self.schematic_grid[row][col])

        elif number > 0:
            self.process_parts(number, gears)
            number = 0
            gears = set()

        return number, gears

    def process_gears(self, row: int, col: int, gears: Set[Tuple[int, int]]) -> None:
        for row_offset in self.ADJACENT_OFFSETS:
            for col_offset in self.ADJACENT_OFFSETS:
                self.process_gear(row, col, row_offset, col_offset, gears)

    def process_gear(self, row: int, col: int, row_offset: int, col_offset: int, gears: Set[Tuple[int, int]]) -> None:
        if self.is_valid_cell(row, col, row_offset, col_offset):
            cell: str = self.schematic_grid[row + row_offset][col + col_offset]

            if self.is_special_symbol(cell):
                gears.add((row + row_offset, col + col_offset))

    def process_parts(self, number: int, gears: Set[Tuple[int, int]]) -> None:
        for gear in gears:
            self.part_counts[gear].append(number)

        if gears:
            self.total_score += number

    def is_valid_cell(self, row: int, col: int, row_offset: int, col_offset: int) -> bool:
        return 0 <= row + row_offset < self.num_rows and 0 <= col + col_offset < self.num_cols

    def is_special_symbol(self, cell: str) -> bool:
        return not cell.isdigit() and cell != '.'

    def is_digit(self, row: int, col: int) -> bool:
        return col < self.num_cols and self.schematic_grid[row][col].isdigit()