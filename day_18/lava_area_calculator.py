from typing import List, Tuple

from direction import Direction


class LavaAreaCalculator:
    def __init__(self, data: str):
        self.dig_plan = self.parse_dig_plan(data)
        
    @staticmethod
    def parse_dig_plan(data: str) -> List[Tuple[Tuple[Direction, int], Tuple[Direction, int]]]:
        DIRECTIONS = {
            'U': Direction(0, -1),
            'D': Direction(0, 1),
            'L': Direction(-1, 0),
            'R': Direction(1, 0)
        }

        result = [
            ((DIRECTIONS[start_direction], int(start_length)), (DIRECTIONS['RDLU'[int(color[-2])]], int(color[2:-2], 16))) 
            for line in data.split('\n') 
            for start_direction, start_length, color in [line.split()]
        ]

        return result
    
    @staticmethod
    def calculate_vertices(dig_plan: List[Tuple[Direction, int]]) -> List[Tuple[int, int]]:
        coord = (0, 0)
        result = [coord]
        
        for direction, length in dig_plan:
            coord =  (direction.delta_row * length) + coord[0],  (direction.delta_column * length) + coord[1]
            result.append(coord)

        return result

    @staticmethod
    def calculate_lava_area(dig_plan: List[Tuple[Direction, int]]) -> int:
        vertices = LavaAreaCalculator.calculate_vertices(dig_plan)
        length = sum(length for _, length in dig_plan)

        green_area = 0
        for start_vertex, end_vertex in zip(vertices, vertices[1:]):
            green_area += start_vertex[0] * end_vertex[1] - end_vertex[0] * start_vertex[1]
        green_area /= 2

        return int(green_area + length / 2 + 1)