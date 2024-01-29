import heapq
from typing import List, Tuple, Dict


class Pathfinder:
    def __init__(self, board_data: str, min_moves: int, max_moves: int):
        self.board = self.parse_board(board_data)
        self.min_moves = min_moves
        self.max_moves = max_moves
        self.start_position = (0, 0)
        self.end_position = max(self.board)
        self.queue = [(0, *self.start_position, 0, 0)]
        self.visited_tiles = set()

    @staticmethod
    def parse_board(board_data: str) -> Dict[Tuple[int, int], int]:
        board = {}
        for row_index, row in enumerate(board_data.split('\n')):
            for column_index, column in enumerate(row.strip()):
                board[(row_index, column_index)] = int(column)

        return board

    def calculate_minimal_heat(self) -> int:
        while self.queue:
            total_heat, current_row, current_column, prev_row, prev_column = heapq.heappop(
                self.queue)

            if (current_row, current_column) == self.end_position:
                return total_heat

            if self.is_visited(current_row, current_column, prev_row, prev_column):
                continue

            self.update_visited_tiles(current_row, current_column, prev_row, prev_column)

            self.calculate_possible_moves(current_row, current_column, prev_row, prev_column, total_heat)

    def calculate_possible_moves(self, current_row: int, current_column: int, prev_row: int, prev_column: int, total_heat: int) -> None:
        possible_moves = self.get_possible_moves(prev_row, prev_column)

        for delta_row, delta_column in possible_moves:
            new_row, new_column, updated_heat = current_row, current_column, total_heat
            self.accumulate_heat(new_row, new_column, delta_row, delta_column, updated_heat)

    def get_possible_moves(self, prev_row: int, prev_column: int) -> List[Tuple[int, int]]:
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        forbidden_moves = [(prev_row, prev_column), (-prev_row, -prev_column)]
        possible_moves = [move for move in [UP, DOWN, LEFT, RIGHT] if move not in forbidden_moves]

        return possible_moves

    def is_visited(self, current_row: int, current_column: int, prev_row: int, prev_column: int) -> bool:
        return (current_row, current_column, prev_row, prev_column) in self.visited_tiles

    def update_visited_tiles(self, current_row: int, current_column: int, prev_row: int, prev_column: int) -> None:
        self.visited_tiles.add(
            (current_row, current_column, prev_row, prev_column))

    def accumulate_heat(self, row: int, column: int, delta_row: int, delta_column: int, heat: int) -> None:
        for index in range(self.max_moves):
            row, column = row + delta_row, column + delta_column

            if (row, column) in self.board:
                heat += self.board[row, column]

                if self.is_least_moves(index):
                    heapq.heappush(self.queue, (heat, row, column, delta_row, delta_column))

    def is_least_moves(self, index: int) -> bool:
        return index + 1 >= self.min_moves
