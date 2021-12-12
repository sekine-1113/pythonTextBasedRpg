class RpgPlayer:
    def __init__(self, name, rank, money, stats) -> None:
        self.name = name
        self.rank = rank
        self.money = money
        self.stats = stats


class RpgQuest:
    def __init__(self, name) -> None:
        self.name = name