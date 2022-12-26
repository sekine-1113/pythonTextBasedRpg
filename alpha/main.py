

class Stats:
    def __init__(self, HP, STR, DEF) -> None:
        self.HP = HP
        self.STR = STR
        self.DEF = DEF


class Actor:
    _id = 0
    def __init__(self, id_: int, name: str, stats: Stats) -> None:
        self._id = self._id+1 if self._id else id_
        self.name = name
        self.stats = stats

    def onTurn(self):
        print(f"{self.name}'s action#")
        print("choose your action:")

    def isDead(self):
        return self.stats.HP <= 0



def onTurn(player: Actor, enemy: Actor):
    player.onTurn()
    enemy.onTurn()

def battle(player: Actor, enemy: Actor):
    while not player.isDead() or enemy.isDead():
        onTurn(player, enemy)
        player.stats.HP -= 10
        enemy.stats.HP -= 100
        if player.isDead():
            return
        if enemy.isDead():
            return




def main():
    player = Actor(0, "a", Stats(200, 100, 100))
    enemy = Actor(0, "b", Stats(200, 20, 20))
    battle(player, enemy)

    return 0


if __name__ == "__main__":
    main()