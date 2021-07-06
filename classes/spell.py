from .useful import Dictable


spells = {
    "Fire": {
        "name": "ファイア",
        "cost": 2,
        "damage": 40,
        "text": "{{}}はファイアを放った!"
    }
}


class Spell(Dictable):
    def __init__(self, name, cost, damage, text=None) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage
        self.text = text


if __name__ == "__main__":
    fire1 = Spell(**spells["Fire"])

    fire = Spell("ファイア", 2, 20)
    print(fire1.asdict())
    print(fire.asdict())