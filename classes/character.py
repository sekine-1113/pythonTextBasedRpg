from classes.useful import Dictable



class Status(Dictable):
    def __init__(self, hp, mp, strength, deffence, luck):
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.deffence = deffence
        self.luck = luck


class Character(Dictable):
    def __init__(self, name: str, status: Status, item: dict, money: int) -> None:
        self.name = name
        self.status = status
        self.item = item
        self.money = money


class Player(Character):
    def __init__(self, name, status, item, money, equipment) -> None:
        super().__init__(name, status, item, money)
        self.equipment = equipment


class Enemy(Character):
    def __init__(self, name, status, item, money) -> None:
        super().__init__(name, status, item, money)


if __name__ == "__main__":
    data = {
        "hp": 32,
        "mp": 0,
        "strength": 16,
        "deffence": 8,
        "luck": 0
    }
    status = Status(
            data["hp"],
            data["mp"],
            data["strength"],
            data["deffence"],
            data["luck"]
    )
    player = Player("プレイヤー", status, {}, 0, 0)
    p = player.asdict()
    print(p)