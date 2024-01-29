from typing import List, Tuple, Dict, Set


class GridSolver:
    def __init__(self, data: List[str]):
        self.grid, self.num_rows = self.parse_grid(data)
        
    @staticmethod
    def parse_grid(data: List[str]) -> Tuple[Dict[Tuple[int, int], str], int]:
        grid = {}
        num_rows = len(data)

        for row_index, row in enumerate(data):
            for column_index, cell_value in enumerate(row):
                if cell_value != '#':
                    grid[(row_index, column_index)] = cell_value

        return grid, num_rows
        
    @staticmethod
    def calculate_modulo(coord: Tuple[int, int], num_rows: int) -> Tuple[int, int]:
        return (coord[0] % num_rows, coord[1] % num_rows)
    
    @staticmethod
    def calculate_arithmetic_sequence_sum(iteration_count: int, initial: int, final: int, increment: int) -> int:
        return initial + iteration_count * (final - initial + (iteration_count - 1) * (increment - final - final + initial) // 2)

    def get_adjacent_cells(self, current_cells: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        new_current_cells = set()

        for direction in [UP, DOWN, LEFT, RIGHT]:
            for position in current_cells:
                new_position = (position[0] + direction[0], position[1] + direction[1])

                if self.calculate_modulo(new_position, self.num_rows) in self.grid:
                    new_current_cells.add(new_position)

        return new_current_cells

    def get_visited_cells_count(self) -> List[int]:
        visited_cells_count = []
        current_cells = set()

        for row, column in self.grid:
            if self.grid[(row, column)] == 'S':
                current_cells.add((row, column))

        for step in range(3 * self.num_rows):
            if step == 64:
                print(len(current_cells))

            if step % self.num_rows == 65:
                visited_cells_count.append(len(current_cells))

            current_cells = self.get_adjacent_cells(current_cells)

        return visited_cells_count

    def calculate_final_result(self) -> int:
        visited_cells_count = self.get_visited_cells_count()
        
        return self.calculate_arithmetic_sequence_sum(26501365 // self.num_rows, *visited_cells_count)