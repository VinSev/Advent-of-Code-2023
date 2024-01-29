from typing import List


class PipeMapper:
    def __init__(self, width: int):
        self.offsets = {
            '|': [width, -width],
            '-': [-1, 1],
            'L': [1, -width],
            'J': [-1, -width],
            '7': [-1, width],
            'F': [1, width],
            '.': [],
            'S': []
        }

    def get_offsets(self, tile: str) -> List[int]:
        return self.offsets[tile]