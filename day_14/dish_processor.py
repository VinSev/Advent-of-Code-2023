from typing import List, Tuple, Dict

from dish import Dish


class DishProcessor:
    def __init__(self, data: str, num_target_cycles: int, num_rotations_per_cycle: int) -> None:
        self.dish = Dish(data)
        self.num_target_cycles = num_target_cycles
        self.num_rotations_per_cycle = num_rotations_per_cycle

    def get_grid_hash(self, grid: List[List[str]]) -> Tuple[Tuple[str]]:
        return tuple(tuple(row) for row in grid)

    def handle_cycle_repetition(self, current_iteration_cycle: int, grid_map: Dict[Tuple[Tuple[str]], int], grid: Tuple[Tuple[str]]) -> int:
        cycle_length = current_iteration_cycle - grid_map[grid]
        amount = (self.num_target_cycles - current_iteration_cycle) // cycle_length
        current_iteration_cycle += amount * cycle_length

        return current_iteration_cycle

    def process_single_cycle(self, current_iteration_cycle: int, grid_hash_map: Dict[Tuple[Tuple[str]], int]) -> int:
        for _ in range(self.num_rotations_per_cycle):
            self.dish.roll()
            self.dish.rotate()

        grid_hash = self.get_grid_hash(self.dish.grid)

        if grid_hash in grid_hash_map:
            current_iteration_cycle = self.handle_cycle_repetition(current_iteration_cycle, grid_hash_map, grid_hash)

        grid_hash_map[grid_hash] = current_iteration_cycle

        return current_iteration_cycle

    def process_dish_cycles(self) -> int:
        grid_hash_map = {}
        current_iteration_cycle = 0

        if self.num_target_cycles == 1 and self.num_rotations_per_cycle == 0:
            self.dish.roll()
            return self.dish.calculate_score()

        while current_iteration_cycle < self.num_target_cycles:
            current_iteration_cycle += 1
            current_iteration_cycle = self.process_single_cycle(current_iteration_cycle, grid_hash_map)

        return self.dish.calculate_score()