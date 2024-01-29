from typing import List


class StepsHashSumCalculator:
    def __init__(self, steps: List[str]):
        self.steps = steps

    def calculate_character_hash(self, index: int, char: str) -> int:
        return (index + ord(char)) * 17 % 256

    def calculate_string_hash(self, step: str) -> int:
        result = 0

        for char in step:
            result = self.calculate_character_hash(result, char)

        return result

    def calculate_steps_hash_sum(self) -> int:
        return sum(self.calculate_string_hash(step) for step in self.steps)