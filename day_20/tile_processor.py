from collections import defaultdict
from math import prod
from typing import Dict, List, Tuple


class TileProcessor:
    def __init__(self, tile_types: Dict[str, Tuple[str, List[str]]], tile_connections: Dict[str, Dict[str, int]], receiver_inputs: Dict[str, int]):
        self.tile_types = tile_types
        self.tile_connections = tile_connections
        self.receiver_inputs = receiver_inputs
        self.tile_flip_states = defaultdict(int)
        self.iterations = 0
        self.tile_counts = [0, 0]

    def process_single_tile(self, tile_queue: List[Tuple[str, str, int]], tile_type: str, input_pulse: int, previous_tile: str, current_tile: str, next_tiles: List[str]) -> List[Tuple[str, str, int]]:
        match tile_type, input_pulse:
            case '', _:
                output_pulse = self.process_empty_module(input_pulse)
            case '%', 0:
                output_pulse = self.process_flip_flop_module(current_tile)
            case '&', _:
                output_pulse, self.receiver_inputs = self.process_conjunction_module(
                    input_pulse, previous_tile, current_tile, next_tiles)
            case _, _:
                return tile_queue

        for next_tile in next_tiles:
            tile_queue.append((current_tile, next_tile, output_pulse))

        return tile_queue

    def process_empty_module(self, input_pulse: int) -> int:
        output_pulse = input_pulse

        return output_pulse

    def process_flip_flop_module(self, current_tile: str) -> int:
        output_pulse = self.tile_flip_states[current_tile] = not self.tile_flip_states[current_tile]

        return output_pulse

    def process_conjunction_module(self, input_pulse: int, previous_tile: str, current_tile: str, next_tiles: List[str]) -> Tuple[int, Dict[str, int]]:
        self.tile_connections[current_tile][previous_tile] = input_pulse
        output_pulse = not all(self.tile_connections[current_tile].values())

        if 'rx' in next_tiles:
            for key, value in self.tile_connections[current_tile].items():
                if value:
                    self.receiver_inputs[key] = self.iterations

        return output_pulse, self.receiver_inputs

    def process_tile_queue(self, tile_queue: List[Tuple[str, str, int]]) -> None:
        while tile_queue:
            previous_tile, current_tile, input_pulse = tile_queue.pop(0)
            self.tile_counts[input_pulse] += 1

            if current_tile not in self.tile_types:
                continue

            tile_type, next_tiles = self.tile_types[current_tile]
            tile_queue = self.process_single_tile(tile_queue, tile_type, input_pulse, previous_tile, current_tile, next_tiles)

    def process_tiles(self) -> None:
        while True:
            if self.iterations == 1000:
                print(prod(self.tile_counts))
            self.iterations += 1

            if all(self.receiver_inputs.values()):
                print(prod(self.receiver_inputs.values()))
                break

            tile_queue = [(None, 'broadcaster', 0)]
            self.process_tile_queue(tile_queue)