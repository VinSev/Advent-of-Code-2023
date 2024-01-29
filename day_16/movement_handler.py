from typing import List, Tuple

class MovementHandler:
    def __init__(self, cell: str, row: int, column: int):
        self.cell = cell
        self.row = row
        self.column = column
        self.delta_row = 0
        self.delta_column = 0

    def handle_movement(self, queue: List[Tuple[int, int, int, int]], delta_row: int, delta_column: int) -> Tuple[int, int]:
        self.delta_row, self.delta_column = delta_row, delta_column
        
        if self.cell == '/':
            self.reverse_direction()
        elif self.cell == '\\':
            self.swap_direction()
        elif self.cell == '-':
            self.handle_horizontal_movement(queue)
        elif self.cell == '|':
            self.handle_vertical_movement(queue)

        return self.delta_row, self.delta_column

    def reverse_direction(self) -> None:
        self.delta_row, self.delta_column = -self.delta_column, -self.delta_row

    def swap_direction(self) -> None:
        self.delta_row, self.delta_column = self.delta_column, self.delta_row

    def handle_horizontal_movement(self, queue: List[Tuple[int, int, int, int]]) -> None:
        if self.delta_row:
            self.delta_row, self.delta_column = 0, 1
            queue.append((self.row, self.column - 1, 0, -1))

    def handle_vertical_movement(self, queue: List[Tuple[int, int, int, int]]) -> None:
        if self.delta_column:
            self.delta_row, self.delta_column = 1, 0
            queue.append((self.row - 1, self.column, -1, 0))