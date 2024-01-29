from typing import List, Dict

from steps_hash_sum_calculator import StepsHashSumCalculator


class StepsProcessor:
    def __init__(self, data: str):
        self.steps = self.parse_steps(data)
        self.hash_boxes = [dict() for _ in range(256)]

    @staticmethod
    def parse_steps(data: str) -> List[str]:
        return data.split(',')

    def process_step(self, step: str):
        parts = step.strip('-').split('=')
        step_hash_sum_calculator = StepsHashSumCalculator([])

        if len(parts) == 1:
            label = parts[0]
            hash_value = step_hash_sum_calculator.calculate_string_hash(label)
            self.hash_boxes[hash_value].pop(label, 0)
        else:
            label, frequency = parts
            hash_value = step_hash_sum_calculator.calculate_string_hash(label)
            self.hash_boxes[hash_value][label] = int(frequency)

    def process_steps(self) -> List[Dict[str, int]]:
        for step in self.steps:
            self.process_step(step)

        return self.hash_boxes

    def calculate_score(self) -> int:
        total_score = 0

        for box_index, box in enumerate(self.hash_boxes, 1):
            for frequency_index, frequency in enumerate(box.values(), 1):
                total_score += box_index * frequency_index * frequency

        return total_score