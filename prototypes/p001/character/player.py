
class Player:

    def __init__(self, name, rank, money, item, role) -> None:
        self.name = name
        self.rank = rank
        self.money = money
        self.item = item
        self.role = role

    def set_rank(self, rank):
        self.rank = rank

    def set_money(self, money):
        self.money = money

    def set_role(self, role):
        self.role = role
