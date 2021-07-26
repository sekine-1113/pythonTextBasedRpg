import os, sys
sys.path.append(os.path.dirname(sys.argv[0]))


from myfunc import *


class Battler:
    def on_turn(self):
        pass


class Wizard:
    def __init__(self) -> None:
        self.name = "Wizard"
        self.health = 0
        self.mana = 0


class Player(Battler):
    def __init__(self, name: str, class_: Wizard) -> None:
        self.name = name
        self.class_ = class_

    def on_turn(self):
        print("choose action.")


class Goblin:
    def __init__(self) -> None:
        self.name = "Goblin"
        self.health = 0
        self.mana = 0


class Enemy(Battler):
    def __init__(self, name: str, class_: Goblin) -> None:
        self.name = name
        self.class_ = class_

    def on_turn(self):
        print("Enemy's action...")


def main():
    db_fp: str = os.path.join(
        os.path.dirname(sys.argv[0]), "database.json"
    )
    db: dict = read_json(db_fp)
    player: Player = Player(db["player"]["name"], Wizard())
    enemy: Enemy = Enemy(db["enemy"]["goblin"]["name"], Goblin())

    while True:
        player.on_turn()
        enemy.on_turn()

        enemy.class_.health = 0

        if enemy.class_.health <= 0:
            break

    print(player.name, "win!")


if __name__ == "__main__":
    main()