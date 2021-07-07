
class Rank:
    def __init__(self, max, min, current) -> None:
        self.max = max
        self.min = min
        self.current = current

    def up(self):
        if self.max > self.current:
            self.current += 1


class Money:
    def __init__(self, max, min, current) -> None:
        self.max = max
        self.min = min
        self.current = current


class Inventory:
    pass


class Role:

    def __init__(self):
        pass


p = {
    "name": "Bob",
    "rank": {
        "max": 20,
        "min": 1,
        "current": 1
    },
    "money": {
        "max": 9999999,
        "min": 0,
        "current": 0
    }
}

class Player:

    def __init__(self, name, rank, money) -> None:
        self.name = name
        self.rank = Rank(**rank)
        self.money = Money(**money)
        self.item = Inventory()
        self.role = Role()
        self.passive = None
        self.equipment = None


class Enemy:

    def __init__(self) -> None:
        self.name = "Bob"
        self.money = Money()
        self.item = Inventory()
        self.role = Role()


def main():
    player = Player(**p)
    print(vars(player))
    print(player.rank.min)
    print(player.rank.current)
    print(player.rank.max)
    player.rank.up()
    print(player.rank.current)

main()