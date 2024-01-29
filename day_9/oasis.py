from typing import List

from extrapolator import Extrapolator


class Oasis:
    def __init__(self, data: str):
        self.report = self.parse_report(data)

    @staticmethod
    def parse_report(data: str) -> List[List[int]]:
        return [[int(element) for element in line.strip().split()] for line in data]

    def calculate_sum_future_extrapolated_values(self) -> int:
        return sum(Extrapolator().extrapolate(line) for line in self.report)

    def calculate_sum_past_extrapolated_values(self) -> int:
        reversed_data = [line[::-1] for line in self.report]

        return sum(Extrapolator().extrapolate(line) for line in reversed_data)
    