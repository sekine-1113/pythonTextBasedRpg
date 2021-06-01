from classes.character import Character


class BattleEngine:
    def __init__(self) -> None:
        self.logics = {}

    def add(self, key, value=None):
        self.logics.setdefault(key, value)

    def get(self, key):
        return self.logics.get(key)

class BattleLogic:
    def __init__(self) -> None:
        self.loop = False

    def _run(self):
        self.loop = True

    def _stop(self):
        self.loop = False

class SingleBattleLogic(BattleLogic):
    def __init__(self, player: Character, enemy: Character) -> None:
        super().__init__()
        self._type = "Single"
        self.player = player
        self.enemy = enemy

    def fight(self):
        self._run()
        while self.loop:
            if self.player.isdead() or self.enemy.isdead():
                self._stop()
            print("LOOPING")


if __name__ == "__main__":
    pass