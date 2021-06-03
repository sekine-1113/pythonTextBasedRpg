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
    def __init__(self) -> None:
        super().__init__()

    def fight(self, player: Character, enemy: Character):
        self._run()
        while self.loop:
            if player.isdead() or enemy.isdead():
                self._stop()
            print("LOOPING")


if __name__ == "__main__":
    player, enemy = Character(), Character()
    logic = SingleBattleLogic(player, enemy)
    logic.fight()