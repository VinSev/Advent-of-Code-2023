from typing import List

from record import Record


class RaceDataParser:
    def parse_race_data(self, data: str) -> List[Record]:
        pass


class PartOneParser(RaceDataParser):
    @staticmethod
    def parse_race_data(data: str) -> List[Record]:
        dirty_times = data[0].split(':')[1]
        dirty_distances = data[1].split(':')[1]

        race_data = [Record(int(time), int(distance)) for time, distance in zip(dirty_times.split(), dirty_distances.split())]

        return race_data


class PartTwoParser(RaceDataParser):
    @staticmethod
    def parse_race_data(data: str) -> List[Record]:
        dirty_time = data[0].replace(' ', '').split(':')[1]
        time = int(dirty_time)

        dirty_distance = data[1].replace(' ', '').split(':')[1]
        distance = int(dirty_distance)

        race_data = [Record(time, distance)]

        return race_data
