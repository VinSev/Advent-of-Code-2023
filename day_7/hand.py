from typing import List, Tuple
from collections import Counter

from hand_strategy import HandStrategy


class Hand:
    CARD_TYPES = 'J23456789TZQKA'
    HAND_TYPES = [
        (1, 1, 1, 1, 1),
        (1, 1, 1, 2),
        (1, 2, 2),
        (1, 1, 3),
        (2, 3),
        (1, 4),
        (5,)
    ]

    def __init__(self, hand_string: str, bid: str) -> None:
        self.hand_string = hand_string
        self.bid = int(bid)

    def evaluate(self, hand_strategy: HandStrategy) -> Tuple[int, List[int]]:
        hand = hand_strategy.replace_card(self.hand_string)
        hand_type = self.calculate_hand_type(hand)
        card_values = self.get_card_values(hand)

        return (hand_type, *card_values)
    
    def calculate_hand_type(self, hand: str) -> int:
        hand_types = []

        for card_strength in self.CARD_TYPES:
            card_counts = Counter(hand.replace('J', card_strength))
            count_values = tuple(sorted(card_counts.values()))
            hand_type = self.HAND_TYPES.index(count_values)
            hand_types.append(hand_type)
            
        return max(hand_types)
    
    def get_card_values(self, hand: str) -> List[int]:
        return [self.CARD_TYPES.index(card) for card in hand]
