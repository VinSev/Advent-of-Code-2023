from typing import List, Set, Tuple


class ScratchCard:
    def __init__(self, card: str):
        self.winning_numbers, self.card_numbers = self.parse_card(card)

    def parse_card(self, card: str) -> Tuple[Set[int], List[int]]:
        _, card = card.split(": ")
        winning_numbers, card_numbers = card.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split()))
        card_numbers = list(map(int, card_numbers.split()))

        return winning_numbers, card_numbers

    def calculate_points(self) -> Tuple[int, int]:
        points = 0
        count = 0

        for number in self.card_numbers:
            if number in self.winning_numbers:
                count += 1
                points = max(points * 2, 1)

        return points, count
