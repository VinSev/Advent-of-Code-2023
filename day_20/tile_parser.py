from collections import defaultdict
from math import prod
from typing import Dict, List, Tuple


class TileParser:
    def __init__(self):
        self.tile_types = {}
        self.tile_connections = defaultdict(dict)
        self.receiver = ''
        self.receiver_inputs = {}

    def parse_tile_id(self, tile_id: str) -> Tuple[str, str]:
        tile_type, tile_id = (tile_id[0], tile_id[1:]) if tile_id[0] in '%&' else ('', tile_id)
        
        return tile_type, tile_id

    def create_tile_types(self, tile_data: List[str]) -> None:
        for line in tile_data:
            tile_id, _, *tile_data = line.replace(',', '').split()
            tile_type, tile_id = self.parse_tile_id(tile_id)
            self.tile_types[tile_id] = tile_type, tile_data

    def create_tile_connections(self, tile_data: List[str]) -> None:
        for line in tile_data:
            tile_id, _, *tile_data = line.replace(',', '').split()
            _, tile_id = self.parse_tile_id(tile_id)

            for data in tile_data:
                self.tile_connections[data][tile_id] = 0

                if data == 'rx':
                    self.receiver = tile_id

    def create_receiver_inputs(self) -> None:
        self.receiver_inputs = {tile_connection: 0 for tile_connection in self.tile_connections[self.receiver]}

    def parse_tiles(self, data: str) -> Tuple[Dict[str, Tuple[str, List[str]]], Dict[str, Dict[str, int]], Dict[str, int]]:
        tile_data = data.split('\n')
        self.create_tile_types(tile_data)
        self.create_tile_connections(tile_data)
        self.create_receiver_inputs()
        
        return self.tile_types, self.tile_connections, self.receiver_inputs