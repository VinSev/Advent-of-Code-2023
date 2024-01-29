from typing import List, Dict, Tuple


class GearRatioStrategy:
    def calculate(self, counts: List[int]) -> int:
        raise NotImplementedError


class TwoCountsGearRatioStrategy(GearRatioStrategy):
    def calculate(self, counts: List[int]) -> int:
        if len(counts) == 2:
            return counts[0] * counts[1]
        return 0


class GearRatiosCalculator:
    def __init__(self, parts: Dict[Tuple[int, int], List[int]], strategies: List[GearRatioStrategy]):
        self.parts = parts
        self.strategies = strategies

    def calculate_gear_ratios(self) -> int:
        total_score = 0

        for _, counts in self.parts.items():
            for strategy in self.strategies:
                total_score += strategy.calculate(counts)

        return total_score
    