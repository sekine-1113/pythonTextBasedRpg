
class Rank:

    def __init__(self, max, min, current) -> None:
        self.max = max
        self.min = min
        self.current = current

    def up(self):
        if self.max > self.current:
            self.current += 1

    def get_next_rank(self):
        pass