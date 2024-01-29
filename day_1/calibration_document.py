from typing import List

word_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


class CalibrationDocument:
    def __init__(self, document: List[str]):
        self.document = document

    def get_calibration_values(self) -> List[str]:
        calibration_values = []

        for amended_value in self.document:
            calibration_value = self.get_calibration_value(amended_value)
            calibration_values.append(calibration_value)

        return calibration_values

    def get_calibration_value(self, amended_value: str) -> str:
        amended_value_numbers = self.convert_line_to_numbers(amended_value)

        if len(amended_value_numbers) == 0:
            return "0"

        first_number = amended_value_numbers[0]
        last_number = amended_value_numbers[-1]

        return str(first_number) + str(last_number)

    def convert_line_to_numbers(self, line) -> List[int]:
        numbers = []
        current_word = ''

        for char in line:
            if char.isdigit():
                numbers.append(char)
                continue

            # --- Added for Second Puzzle
            current_word += char

            for key, value in word_to_number.items():
                if key in current_word:
                    numbers.append(value)
                    current_word = '' + char
            # ---

        return numbers

    def sum_calibration_values(self, calibration_values: List[str]) -> int:
        return sum(int(element) for element in calibration_values)
