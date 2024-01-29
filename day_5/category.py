from typing import List

from range import Range


class Category:
    def __init__(self, destination, source, size):
        self.destination = destination
        self.source = source
        self.size = size

    def is_source_in_category(self, value: int) -> bool:
        return self.source <= value < self.source + self.size

    def calculate_new_source(self, value: int) -> int:
        return value + self.destination - self.source
    
    def process_ranges(self, ranges: List[Range], results: List[Range]) -> List[Range]:
        new_ranges = []

        for rng in ranges:
            new_ranges += self.process_range(rng, results)

        return new_ranges
    
    def process_range(self, rng: List[Range], results: List[Range]) -> List[Range]:
        new_ranges = []
        
        before_ranges = self.process_start_range(rng)
        new_ranges += before_ranges

        self.process_middle_range(rng, results)

        after_ranges = self.process_end_range(rng)
        new_ranges += after_ranges
        
        return new_ranges

    def process_start_range(self, rng: Range) -> List[Range]:
        start_range = Range(rng.start, min(rng.end, self.source))

        if start_range.end > start_range.start:
            return [start_range]

        return []

    def process_middle_range(self, rng: Range, results: List[Range]) -> None:
        middle_range = Range(max(rng.start, self.source), 
                             min(self.source + self.size, rng.end))

        if middle_range.end > middle_range.start:
            result = Range(middle_range.start - self.source + self.destination, 
                           middle_range.end - self.source + self.destination)
            results.append(result)

    def process_end_range(self, rng: Range) -> List[Range]:
        end_range = Range(max(self.source + self.size, 
                              rng.start), rng.end)

        if end_range.end > end_range.start:
            return [end_range]

        return []
