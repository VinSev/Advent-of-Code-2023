class HandStrategy:
    def replace_card(self, hand_string: str) -> str:
        pass


class Part1HandStrategy(HandStrategy):
    def replace_card(self, hand_string: str) -> str:
        return hand_string.replace('J', 'Z')


class Part2HandStrategy(HandStrategy):
    def replace_card(self, hand_string: str) -> str:
        return hand_string
