from collections import deque, defaultdict
from typing import List, Tuple, Dict, Set

from grid import Grid


class Pathfinder:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.edges, self.reverse_edges = self.bfs()

    def explore_neighbors(self, visited: Set[Tuple[int, int]], queue: deque, steps: int, position: Tuple[int, int], previous_split: Tuple[int, int]) -> Tuple[deque, Set[Tuple[int, int]]]:
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        
        directions = {'^': UP, 'v': DOWN, '<': LEFT, '>': RIGHT}

        for delta_row, delta_column in [UP, DOWN, LEFT, RIGHT]:
            new_position = (position[0] + delta_row, position[1] + delta_column)

            if new_position not in self.grid.ground_map or self.grid.ground_map[new_position] == '#':
                continue

            if self.grid.ground_map[new_position] in directions and (delta_row, delta_column) != directions[self.grid.ground_map[new_position]]:
                continue

            if new_position in self.grid.splits or new_position not in visited:
                visited.add(new_position)
                queue.append((steps + 1, new_position, previous_split))

        return queue, visited

    def bfs(self) -> Tuple[Dict[Tuple[int, int], Set[Tuple[Tuple[int, int], int]]], Dict[Tuple[int, int], Set[Tuple[Tuple[int, int], int]]]]:
        STARTING_POS = (0, 1)
        queue = deque()
        queue.append((0, STARTING_POS, STARTING_POS))

        visited = set()

        edges = defaultdict(set)
        reverse_edges = defaultdict(set)

        while queue:
            steps, position, previous_split = queue.pop()

            if position == previous_split or position not in self.grid.splits:
                queue, visited = self.explore_neighbors(visited, queue, steps, position, previous_split)
                continue

            queue.append((0, position, position))
            edges[previous_split].add((position, steps))
            reverse_edges[position].add((previous_split, steps))

        return edges, reverse_edges

    def add_neighbors_to_queue(self, use_reverse: bool, queue: deque, steps: int, position: Tuple[int, int], path: Set[Tuple[int, int]]) -> deque:
        neighbors = self.edges[position]

        if use_reverse:
            neighbors = neighbors.union(self.reverse_edges[position])

        for neighbor, weight in neighbors:
            if neighbor in path:
                continue

            queue.append((steps + weight, neighbor, path.union({neighbor})))

        return queue

    def find_max_steps(self, use_reverse: bool) -> int:
        queue = deque([(0, (0, 1), {(0, 1)})])
        max_steps = 0

        while queue:
            steps, position, path = queue.pop()

            if position != (self.grid.num_rows - 1, self.grid.num_columns - 2):
                queue = self.add_neighbors_to_queue(use_reverse, queue, steps, position, path)
                continue

            max_steps = max(steps, max_steps)

        return max_steps