from typing import List

from race_data_parser import RaceDataParser
from record import Record


class BoatRace:
    SPEED_INCREASE_PER_MILLISECOND = 1

    def __init__(self, data: str, parser: RaceDataParser):
        self.records = parser.parse_race_data(data)

    def calculate_ways_to_win(self) -> List[int]:
        return [self.calculate_ways_to_win_for_record(record) for record in self.records]

    def calculate_ways_to_win_for_record(self, record: Record) -> int:
        amount_of_ways_to_win = 0

        for milliseconds in range(0, record.time + 1):
            speed = milliseconds * BoatRace.SPEED_INCREASE_PER_MILLISECOND
            distance = speed * (record.time - milliseconds)

            if distance > record.distance:
                amount_of_ways_to_win += 1

        return amount_of_ways_to_win
