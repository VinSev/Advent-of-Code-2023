from hailstone import Hailstone


class CollisionChecker:
    def check_collision(self, first_hailstone: Hailstone, second_hailstone: Hailstone) -> bool:
        collision_area_start = 200000000000000
        collision_area_end = 400000000000000

        position_first, velocity_first = first_hailstone.position, first_hailstone.velocity
        position_second, velocity_second = second_hailstone.position, second_hailstone.velocity

        cross_product = velocity_first.x * velocity_second.y - velocity_first.y * velocity_second.x

        if cross_product == 0:
            return self.check_parallel_collision(position_first, velocity_first, position_second)

        time_to_collision_second = self.calculate_time_to_collision_second(position_first, velocity_first, position_second, cross_product)

        time_to_collision_first = self.calculate_time_to_collision_first(position_first, velocity_first, position_second, velocity_second, time_to_collision_second)

        if time_to_collision_first < 0 or time_to_collision_second < 0:
            return False

        collision_point = self.calculate_collision_point(position_second, velocity_second, time_to_collision_second)

        return self.is_within_collision_area(collision_point, collision_area_start, collision_area_end)

    @staticmethod
    def check_parallel_collision(position_first: tuple, velocity_first: tuple, position_second: tuple) -> bool:
        return velocity_first.x * (position_first.y - position_second.y) + velocity_first.y * (position_second.x - position_first.x) == 0

    @staticmethod
    def calculate_time_to_collision_second(position_first: tuple, velocity_first: tuple, position_second: tuple, cross_product: int) -> float:
        return (velocity_first.x * (position_first.y - position_second.y) + velocity_first.y * (position_second.x - position_first.x)) / cross_product

    @staticmethod
    def calculate_time_to_collision_first(position_first: tuple, velocity_first: tuple, position_second: tuple, velocity_second: tuple, time_to_collision_second: float) -> float:
        return (position_second.x - position_first.x + velocity_second.x * time_to_collision_second) / velocity_first.x

    @staticmethod
    def calculate_collision_point(position_second: tuple, velocity_second: tuple, time_to_collision_second: float) -> tuple:
        return (
            position_second.x + velocity_second.x * time_to_collision_second,
            position_second.y + velocity_second.y * time_to_collision_second
        )

    @staticmethod
    def is_within_collision_area(collision_point: tuple, collision_area_start: int, collision_area_end: int) -> bool:
        return (
            collision_area_start <= collision_point[0] <= collision_area_end and
            collision_area_start <= collision_point[1] <= collision_area_end
        )
