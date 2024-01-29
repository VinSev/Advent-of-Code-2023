from typing import List

from category import Category
from range import Range


class Mapping:
    def __init__(self, map: str):
        self.categories: List[Category] = self.parse_categories(map)

    @staticmethod
    def parse_categories(mapping: str) -> List[Category]:
        categories = mapping.split('\n')[1:]

        return [Category(*[int(value) for value in category.split()]) for category in categories]

    def calculate_new_source(self, source: int) -> int:
        for category in self.categories:
            if category.is_source_in_category(source):
                return category.calculate_new_source(source)

        return source

    def process_ranges(self, ranges: List[Range]) -> List[Range]:
        results = []

        for category in self.categories:
            ranges = category.process_ranges(ranges, results)

        return results + ranges
