from typing import Tuple, List

from mapping import Mapping
from range import Range


class Almanac:
    def __init__(self, data: str):
        self.seeds, self.mappings = self.parse_data(data)
        
    def parse_data(self, data: str) -> Tuple[List[int], List[Mapping]]:
        seed_data, *mapping_data = data.split('\n\n')
        seeds = self.parse_seeds(seed_data)
        mappings = self.parse_mappings(mapping_data)
        
        return seeds, mappings
        
    @staticmethod
    def parse_seeds(data: str) -> List[int]:
        dirty_seeds = data.split(':')[1]
        seeds = [int(seed) for seed in dirty_seeds.split()]

        return seeds

    @staticmethod
    def parse_mappings(mappings: str) -> List[Mapping]:
        return [Mapping(mapping) for mapping in mappings]

    def calculate_locations(self) -> List[int]:
        locations = []

        for source in self.seeds:
            for mapping in self.mappings:
                source = mapping.calculate_new_source(source)
            locations.append(source)

        return locations

    def calculate_ranges(self) -> List[int]:
        processed_ranges = []
        pairs = self.get_seed_pairs()

        for start, size in pairs:
            ranges = [Range(start, start + size)]

            for mapping in self.mappings:
                ranges = mapping.process_ranges(ranges)
            processed_ranges.append(min(ranges).start)

        return processed_ranges
    
    def get_seed_pairs(self) -> List[Tuple[int, int]]:
        return list(zip(self.seeds[::2], self.seeds[1::2]))
