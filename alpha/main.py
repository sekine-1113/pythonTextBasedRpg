from typing import Generic, TypeVar


class Stats:
    def __init__(self, HP: int, STR: int, DEF: int) -> None:
        assert isinstance(HP, int)
        assert isinstance(STR, int)
        assert isinstance(DEF, int)
        self.HP = HP
        self.STR = STR
        self.DEF = DEF
        assert isinstance(self.HP, int)
        assert isinstance(self.STR, int)
        assert isinstance(self.DEF, int)


class Actor:
    def __init__(self, name: str, stats: Stats) -> None:
        self.name = name
        self.stats = stats

    def onTurn(self):
        print(f"{self.name}'s action#")
        print("choose your action:")

    def isDead(self):
        return self.stats.HP <= 0

    def __repr__(self) -> str:
        return f"{self.name}"



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
    player = Actor("a", Stats(200, 100, 100))
    enemy = Actor("b", Stats(200, 20, 20))
    battle(player, enemy)

    return 0


if __name__ == "__main__":
    main()