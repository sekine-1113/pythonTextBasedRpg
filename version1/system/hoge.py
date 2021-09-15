from abc import ABC, abstractmethod

from version1.system.battle import fight


class BaseCharacter(ABC):
    def __init__(self, name: str, status: dict[str, object]) -> None:
        self.name = name
        self.status = status

    @abstractmethod
    def action(self):
        ...


class Player(BaseCharacter):
    def __init__(self, name: str, status: dict[str, object]) -> None:
        super().__init__(name, status)

    def action(self):
        print(self.name, "action")
        return super().action()


class Enemy(BaseCharacter):
    def __init__(self, name: str, status: dict[str, object]) -> None:
        super().__init__(name, status)

    def action(self):
        print(self.name, "action")
        return super().action()


if __name__ == "__main__":
    pinfo = {"name": "Alice", "status": {}}
    einfo = {"name": "Enemy", "status": {}}
    player = Player(pinfo["name"], pinfo["status"])
    enemy = Enemy(einfo["name"], einfo["status"])
    fight(player, enemy)