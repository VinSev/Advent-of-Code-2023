from typing import List

from hand import Hand
from hand_strategy import HandStrategy


class CamelCardsGame:
    def __init__(self, data: List[str], hand_strategy: HandStrategy) -> None:
        self.hands = self.parse_hands(data)
        self.hand_strategy = hand_strategy

    @staticmethod
    def parse_hands(hand_data: str) -> List[Hand]:
        hands = []

        for hand in hand_data:
            hand_string, bid = hand.strip().split()
            hands.append(Hand(hand_string, bid))

        return hands

    def order_hands(self) -> None:
        self.hands.sort(key=lambda hand: hand.evaluate(self.hand_strategy))

    def calculate_score(self) -> int:
        total_score = 0

        for i, hand in enumerate(self.hands):
            total_score += hand.bid * (i + 1)

        return total_score
