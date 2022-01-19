
class Weapon:
    def __init__(self, name, attack) -> None:
        self.name = name
        self.attack = attack

    def __str__(self) -> str:
        return f"Name: {self.name} ATK:{self.attack}"

class Ability:
    def effect(self):
        print("effect!")

class IActor:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

class Player(IActor):
    def __init__(self, name, weapon) -> None:
        super().__init__(name)
        self.weapon = weapon

class Enemy(IActor):
    def __init__(self, name) -> None:
        super().__init__(name)


class Engine:
    def __init__(self) -> None:
        self.player = None
        self.enemy = None

    def set_actor(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print("start")
        print(self.player)


class BattleEngine:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def set_actor(self, player, enemy):
        self.engine.set_actor(player, enemy)
        return self

    def battle(self):
        self.engine.start()


BattleEngine(Engine()).set_actor(Player("アリス", Weapon("ナイフ", 8)), Enemy("ゴブリン")).battle()