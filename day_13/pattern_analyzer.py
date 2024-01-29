from typing import List


class PatternAnalyzer:
    def __init__(self, data: str):
        self.patterns = self.parse_patterns(data)

    @staticmethod
    def parse_patterns(data: str) -> List[List[List[str]]]:
        return [[list(row) for row in pattern.split('\n')] for pattern in data.split('\n\n')]

    @staticmethod
    def is_valid_column_range(left_column: int, right_column: int, num_columns: int) -> bool:
        return 0 <= left_column < right_column < num_columns

    def analyze_reflection(self, has_smudges: bool) -> int:
        total_reflection = 0

        for pattern in self.patterns:
            total_reflection += self.check_vertical_symmetry(pattern, has_smudges)
            total_reflection += self.check_horizontal_symmetry(pattern, has_smudges)

        return total_reflection

    def check_vertical_symmetry(self, pattern: List[List[str]], has_smudges: bool) -> int:
        num_rows = len(pattern)
        num_columns = len(pattern[0])

        total_reflection = 0

        for column in range(num_columns - 1):
            symmetry_count = self.count_symmetry_column(
                pattern, num_rows, num_columns, column)

            if symmetry_count == has_smudges:
                total_reflection += column + 1

        return total_reflection

    def check_horizontal_symmetry(self, pattern: List[List[str]], has_smudges: bool) -> int:
        transposed_pattern = list(zip(*pattern))
        return self.check_vertical_symmetry(transposed_pattern, has_smudges) * 100

    def count_symmetry_column(self, pattern: List[List[str]], num_rows: int, num_columns: int, column: int) -> int:
        symmetry_count = 0

        for column_distance in range(num_columns):
            left_column = column - column_distance
            right_column = column + 1 + column_distance

            if self.is_valid_column_range(left_column, right_column, num_columns):
                symmetry_count += self.compare_columns_within_range(
                    pattern, left_column, right_column, num_rows)

        return symmetry_count

    def compare_columns_within_range(self, pattern: List[List[str]], left_column: int, right_column: int, num_rows: int) -> int:
        symmetry_count = 0

        for row_index in range(num_rows):
            if pattern[row_index][left_column] != pattern[row_index][right_column]:
                symmetry_count += 1

        return symmetry_count