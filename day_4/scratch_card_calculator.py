from typing import List, Tuple

from scratch_card import ScratchCard


class Copies:
    def __init__(self, count: int):
        self.copies = [1] * count

    def update(self, card_index: int, count: int) -> None:
        for copy_index in range(card_index + 1, card_index + count + 1):
            self.copies[copy_index] += self.copies[card_index]

    def calculate_total(self) -> int:
        return sum(self.copies)


class ScratchCardCollection:
    def __init__(self, card_strings: List[str]):
        self.scratch_cards = [ScratchCard(card_string)
                              for card_string in card_strings]

    def __iter__(self):
        return iter(self.scratch_cards)

    def __len__(self):
        return len(self.scratch_cards)


class ScratchCardCalculator:
    def __init__(self):
        self.total_points = 0
        self.copies = None

    def calculate_total_points(self, scratch_cards: ScratchCardCollection) -> None:
        for card_index, card in enumerate(scratch_cards):
            self.calculate_points_for_card(card_index, card)

    def calculate_points_for_card(self, card_index: int, card: ScratchCard) -> None:
        points, count = card.calculate_points()
        self.copies.update(card_index, count)
        self.total_points += points

    def calculate_scratch_cards(self, card_strings: List[str]) -> Tuple[int, int]:
        scratch_cards = ScratchCardCollection(card_strings)
        self.copies = Copies(len(scratch_cards))
        self.calculate_total_points(scratch_cards)

        total_copies = self.copies.calculate_total()
        return self.total_points, total_copies
