

enemies = [
    {"name": "Goblin"}
]

class Goblin:
    def __init__(self, health, mana, nickname=None) -> None:
        self.__name = "Goblin"
        self._nickname = nickname
        self.health = health
        self.mana = mana

    @property
    def name(self):
        return self.__name

    def echo_nickname_and_name(self):
        print(self._nickname, "of", self.__name)


goblin = Goblin(60, 20, "Bob")
print(goblin.name)
print(goblin.health)
print(goblin.mana)