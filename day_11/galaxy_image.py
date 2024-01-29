from typing import List, Tuple, Set


class GalaxyImage:
    GALAXY = "#"
    EMPTY_SPACE = '.'

    def __init__(self, galaxy_image: str, growth_rate: int) -> None:
        self.galaxy_image = self.parse_galaxy_image(galaxy_image)
        self.growth_rate = growth_rate

    @staticmethod
    def parse_galaxy_image(galaxy_image: str) -> List[List[str]]:
        return [[space for space in line] for line in galaxy_image.split()]

    def calculate_distance(self, origin: Tuple[int, int], destination: Tuple[int, int]) -> int:
        return sum(abs(x - y) for x, y in zip(origin, destination))

    def find_empty_row_indices(self) -> Set[int]:
        return {
            i for i, row in enumerate(self.galaxy_image)
            if all(space == self.EMPTY_SPACE for space in row)
        }

    def find_empty_column_indices(self) -> Set[int]:
        return {
            i for i, col in enumerate(zip(*self.galaxy_image))
            if all(space == self.EMPTY_SPACE for space in col)
        }

    def find_galaxy_coordinates(self) -> List[Tuple[int, int]]:
        empty_row_indices = self.find_empty_row_indices()
        empty_column_indices = self.find_empty_column_indices()
        galaxy_coordinates = []

        row_offset = 0

        for i, row in enumerate(self.galaxy_image):
            if i in empty_row_indices:
                row_offset += self.growth_rate - 1

            column_offset = 0

            for j, space in enumerate(row):
                if j in empty_column_indices:
                    column_offset += self.growth_rate - 1

                if space == self.GALAXY:
                    galaxy_coordinates.append(
                        (i + row_offset, j + column_offset))

        return galaxy_coordinates

    def calculate_sum_distances(self) -> int:
        galaxy_coordinates = self.find_galaxy_coordinates()

        return sum(
            self.calculate_distance(origin, destination)
            for i, origin in enumerate(galaxy_coordinates[:-1])
            for destination in galaxy_coordinates[i + 1:]
        )
