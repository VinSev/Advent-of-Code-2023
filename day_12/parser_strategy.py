from typing import List, Tuple


class ParserStrategy:
    def parse(self, line: str) -> Tuple[List[str], List[int]]:
        raise NotImplementedError

class DefaultParserStrategy(ParserStrategy):
    def parse(self, line: str) -> Tuple[List[str], List[int]]:
        springs, groups = line.split()
        springs = [spring for spring in springs]
        groups = [int(group) for group in groups.split(',')]
        
        return springs, groups

class UnfoldParserStrategy(ParserStrategy):
    def parse(self, line: str) -> Tuple[List[str], List[int]]:
        springs, groups = line.split()
        springs = '?'.join([springs] * 5)
        springs = [spring for spring in springs]
        groups = ','.join([groups] * 5)
        groups = [int(group) for group in groups.split(',')]
        
        return springs, groups