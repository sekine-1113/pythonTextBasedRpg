
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
    def __init__(self, name, abilities) -> None:
        self.name = name
        self.abilities = abilities

    def __str__(self) -> str:
        return f"{self.name}"

class Player(IActor):
    def __init__(self, name, abilities, weapon) -> None:
        super().__init__(name, abilities)
        self.weapon = weapon

class Enemy(IActor):
    def __init__(self, name, abilities) -> None:
        super().__init__(name, abilities)


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
        return 0


class Battle:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def set_actor(self, player, enemy):
        self.engine.set_actor(player, enemy)
        return self

    def battle(self):
        self.engine.start()
        return 0



Battle(
    Engine()
).set_actor(
    Player(
        "アリス",
        [Ability()],
        Weapon("ナイフ", 8)
    ),
    Enemy(
        "ゴブリン",
        [Ability()]
    )
).battle()