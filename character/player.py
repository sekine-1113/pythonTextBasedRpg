
class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.rank = None
        self.money = None
        self.item = None
        self.role = None
        self.passive = None
        self.equipment = None

    def set_rank(self, rank):
        self.rank = rank

    def set_money(self, money):
        self.money = money
