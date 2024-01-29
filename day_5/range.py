class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
    def __lt__(self, other_range):
        return self.start < other_range.start   
