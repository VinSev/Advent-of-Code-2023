from typing import List
import numpy as np
from numpy import ndarray


class Extrapolator:
    @staticmethod
    def accumulate_lines(stack: List[ndarray]) -> List[ndarray]:
        for _ in range(len(stack) - 1):
            current_line = stack.pop()
            stack[-1] = stack[-1] + current_line[-1]

        return stack

    @staticmethod
    def calculate_differences_of_stack(stack: List[ndarray]) -> List[ndarray]:
        line = stack[-1]

        while not np.all(line == 0):
            line = stack[-1]
            difference = np.diff(line)
            stack.append(difference)

        return stack

    def extrapolate(self, line: List[int]) -> int:
        stack = [np.array(line)]

        stack = self.calculate_differences_of_stack(stack)

        stack[-1] = np.append(stack[-1], 0)
        stack = self.accumulate_lines(stack)

        return stack[0][-1]