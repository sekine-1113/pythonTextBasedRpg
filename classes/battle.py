
from classes.character import Character


class BattleEngine:
    pass

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
        self.player = player
        self.enemy = enemy

    def fight(self):
        self._run()
        while self.loop:
            if self.player.isdead() or self.enemy.isdead():
                self._stop()
            print("LOOPING")

