from typing import List, Tuple, Set


class BrickProcessor():
    def __init__(self, data: List[str]):
        self.bricks = self.create_bricks(data)
        self.dropped_bricks, _ = self.drop_bricks(self.bricks)
        
    @staticmethod
    def create_brick(start: Tuple[int, int, int], end: Tuple[int, int, int]) -> Set[Tuple[int, int, int]]:
        brick = set([start, end])
        
        for axis in range(2):
            if start[axis] != end[axis]:
                for position in range(min(start[axis], end[axis]) + 1, max(start[axis], end[axis])):
                    to_add = list(start)
                    to_add[axis] = position
                    brick.add(tuple(to_add))
                    
        return brick

    def create_bricks(self, data: List[str]) -> List[Set[Tuple[int, int, int]]]:
        bricks = []
        
        for line in data:
            start, end = line.split("~")
            start_coordinates = tuple(map(int, start.split(",")))
            end_coordinates = tuple(map(int, end.split(",")))
            brick = self.create_brick(start_coordinates, end_coordinates)
            bricks.append(brick)
            
        return bricks

    def sort_bricks(self, bricks: List[Set[Tuple[int, int, int]]]) -> List[Set[Tuple[int, int, int]]]:
        return sorted(bricks, key=lambda bricks: min(brick[2] for brick in bricks))

    def move_brick(self, brick: Set[Tuple[int, int, int]], settled: Set[Tuple[int, int, int]]) -> Tuple[Set[Tuple[int, int, int]], bool]:
        did_move = False
        
        while True:
            next_position = set((x, y, z - 1) for x, y, z in brick)
            
            if all((cube[2] != 0 and (cube not in settled)) for cube in next_position):
                brick = next_position
                did_move = True
            else:
                break
            
        for cube in brick:
            settled.add(cube)
            
        return brick, did_move

    def drop_bricks(self, bricks: List[Set[Tuple[int, int, int]]]) -> Tuple[List[Set[Tuple[int, int, int]]], int]:
        sorted_bricks = self.sort_bricks(bricks)
        settled = set()
        final_bricks = []
        num_fell = 0
        
        for brick in sorted_bricks:
            brick, did_move = self.move_brick(brick, settled)
            final_bricks.append(brick)
            
            if did_move:
                num_fell += 1
                
        return final_bricks, num_fell

    def calculate_total_bricks(self) -> Tuple[int, int]:
        total_stable_bricks = 0
        total_fallen_bricks = 0
        
        for brick in self.dropped_bricks:
            num_fell = 0
            filtered_bricks = []
            
            for dropped_brick in self.dropped_bricks:
                if dropped_brick != brick:
                    filtered_bricks.append(dropped_brick)
                    
            if self.drop_bricks(filtered_bricks)[1] == 0:
                total_stable_bricks += 1
                    
            num_fell = self.drop_bricks(filtered_bricks)[1]
            total_fallen_bricks += num_fell
        
        return total_stable_bricks, total_fallen_bricks