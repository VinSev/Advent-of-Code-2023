from typing import List, Tuple, Optional, Set

from pipe_mapper import PipeMapper


class PipeMazeSolver:
    def __init__(self, sketch: str):
        self.pipe_mapper = PipeMapper(self.width)
        self.width, self.height, self.tiles = self.parse_data(sketch)
        self.start = self.find_start()
        self.path, self.tiles = self.create_path()

    @staticmethod
    def parse_data(sketch):
        width = len(sketch[0])
        height = len(sketch)
        tiles = ''.join(sketch)

        return width, height, tiles

    def find_start(self) -> Optional[int]:
        return next((index for index, tile in enumerate(self.tiles) if tile == 'S'), None)

    def create_path(self) -> Tuple[Set[int], List[List[int]]]:
        path = {self.start}
        data = [self.pipe_mapper.get_offsets(tile) for tile in self.tiles]

        for index, offsets in enumerate(data):
            if self.start in (index + offset for offset in offsets):
                self.pipe_mapper.get_offsets('S').append(index - self.start)

        return path, data

    def bfs(self) -> int:
        queue = [(next(iter(self.path)), 0)]
        max_depth = 0

        while queue:
            position, depth = queue.pop(0)
            max_depth = max(max_depth, depth)

            for offset in self.tiles[position]:
                new_position = position + offset

                if new_position not in self.path:
                    self.path.add(new_position)
                    queue.append((new_position, depth + 1))

        return max_depth

    def is_outside_right(self, position: int) -> bool:
        return position in self.path and 1 in self.tiles[position]

    def is_outside_left(self, position: int) -> bool:
        return position in self.path and -1 in self.tiles[position]

    def is_inside_loop(self, position: int) -> bool:
        outside_right = outside_left = True

        while position > 0:
            if self.is_outside_right(position):
                outside_right = not outside_right

            if self.is_outside_left(position):
                outside_left = not outside_left

            position -= self.width

        return not (outside_right or outside_left)

    def count_tiles_inside_loop(self) -> int:
        inside = 0

        for tile in range(len(self.tiles)):
            if tile in self.path:
                continue

            if self.is_inside_loop(tile):
                inside += 1

        return inside