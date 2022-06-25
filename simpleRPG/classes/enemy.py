from games.cui.textbasedrpg.simpleRPG.interface.enemy import IEnemy


class Enemy(IEnemy):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class MockEnemy(IEnemy):
    def __init__(self, name: str = "Mock") -> None:
        super().__init__(name)