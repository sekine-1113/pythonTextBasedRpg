class StatValue:
    def __init__(self, val) -> None:
        self.val = val

    def add(self, val):
        print("added", val, "total", self.val + val)
        return StatValue(self.val + val)

class Stats:
    def __init__(self, HP, ATK) -> None:
        self.HP = HP
        self.ATK = ATK

class Inventory:
    pass

class Skill:
    pass

class Player:
    def __init__(self, name, stats) -> None:
        self.name = name
        self.stats = stats


player = Player("Alice", Stats(StatValue(300), StatValue(120)))
print(player.stats.HP.val)
player.stats.HP = player.stats.HP.add(200)
