from typing import List


class Arrangement:
    DAMAGED = '.'
    OPERATIONAL = '#'
    UNKNOWN = '?'
    
    def __init__(self, springs: List[str], groups: List[int]):
        self.springs = springs
        self.groups = groups 
        self.arrangement_cache = {}
        
    def is_arrangement_complete(self, spring_index: int, group_index: int, count: int) -> int:
        if spring_index == len(self.springs):
            if group_index == len(self.groups) and count == 0:
                return 1
            
            if group_index == len(self.groups) - 1 and self.groups[group_index] == count:
                return 1
            
            return 0
    
    def process_damaged_spring(self, spring_index: int, group_index: int, count: int) -> int:
        total_count = 0
        
        if count == 0:
            total_count += self.process_arrangement(spring_index + 1, group_index, 0)
            
        if count > 0 and group_index < len(self.groups) and self.groups[group_index] == count:
            total_count += self.process_arrangement(spring_index + 1, group_index + 1, 0)
            
        return total_count

    def process_operational_spring(self, spring_index: int, group_index: int, count: int) -> int:
        return self.process_arrangement(spring_index + 1, group_index, count + 1)

    def count_arrangement(self, spring_index: int, group_index: int, count: int) -> int:
        total_count = 0

        for spring_type in [self.DAMAGED, self.OPERATIONAL]:
            if self.springs[spring_index] == spring_type or self.springs[spring_index] == self.UNKNOWN:
                if spring_type == self.DAMAGED:
                    total_count += self.process_damaged_spring(spring_index, group_index, count)
                    
                if spring_type == self.OPERATIONAL:
                    total_count += self.process_operational_spring(spring_index, group_index, count)

        return total_count

    def process_arrangement(self, spring_index: int, group_index: int, count: int) -> int:
        key = (spring_index, group_index, count)
        
        if key in self.arrangement_cache:
            return self.arrangement_cache[key]
        
        arrangement_complete = self.is_arrangement_complete(spring_index, group_index, count)
        if arrangement_complete is not None:
            return arrangement_complete
            
        total_count = self.count_arrangement(spring_index, group_index, count)
                    
        self.arrangement_cache[key] = total_count
        
        return total_count