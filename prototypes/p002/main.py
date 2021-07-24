import os, sys
import json

def read_json(fp):
    with open(fp, "r", encoding="UTF-8") as f:
        return json.load(f)


class Wizard:
    def __init__(self) -> None:
        self.name = "Wizard"
        self.health = 0
        self.mana = 0


class Player:
    def __init__(self, name: str, class_: Wizard) -> None:
        self.name = name
        self.class_ = class_


class Goblin:
    def __init__(self) -> None:
        self.name = "Goblin"
        self.health = 0
        self.mana = 0


class Enemy:
    def __init__(self, name: str, class_: Goblin) -> None:
        self.name = name
        self.class_ = class_


def main():
    db_fp: str = os.path.join(os.path.dirname(sys.argv[0]), "database.json")
    db: dict = read_json(db_fp)
    player: Player = Player(db["player"]["name"], Wizard())
    enemy: Enemy = Enemy(db["enemy"]["goblin"]["name"], Goblin())
    print(player.class_.name)
    print(enemy.class_.name)


if __name__ == "__main__":
    main()