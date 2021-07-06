
from copy import deepcopy


enemies = {
    "name": "goblin",
    "id": 0,
    "stats": {
        "maxHP": 1200,
        "HP": 1200,
        "maxMP": 200,
        "MP": 200,
        "STR": 120,
        "MSTR": 360,
        "DEFF": 80,
        "MDEFF": 160,
        "EXP": 4
    }
}

class Enemy:
    def __init__(self, id: int, name: str, stats: dict) -> None:
        self.id = id
        self.name = name
        self.stats = stats

    def debug(self):
        for k, v in vars(self).items():
            print(k, v)

    def create(self):
        from copy import deepcopy
        return deepcopy(self)



if __name__ == "__main__":
    enemyInfo = Enemy(**enemies)
    enemy = enemyInfo.create()
    enemy.debug()
    enemy.stats["HP"] -= 1000
    enemy.debug()
    enemy = enemyInfo.create()
    enemy.debug()

