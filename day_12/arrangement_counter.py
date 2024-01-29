from typing import List, Tuple

from parser_strategy import ParserStrategy
from arrangement import Arrangement


class ArrangementCounter:
    def __init__(self, data: str, parser_strategy: ParserStrategy):
        self.parser_strategy = parser_strategy
        self.parsed_data = self.parse_data(data)
        
    def parse_data(self, data: str) -> List[Tuple[List[str], List[int]]]:
        parsed_data = []
        
        for line in data:
            springs, groups = self.parser_strategy.parse(line)
            parsed_data.append((springs, groups))
            
        return parsed_data

    def count_total_arrangements(self) -> int:
        total_arrangements = 0
        
        for springs, groups in self.parsed_data:
            arrangement = Arrangement(springs, groups)
            arrangements = arrangement.count_arrangement(0, 0, 0)
            total_arrangements += arrangements
            
        return total_arrangements