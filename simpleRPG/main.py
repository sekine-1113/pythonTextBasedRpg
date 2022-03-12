
class Player:
    def __init__(self, name) -> None:
        self.name = name

class Enemy:
    def __init__(self, name) -> None:
        self.name = name


class Main:
    def __init__(self) -> None:
        self._player: Player = Player("Alice")
        self._enemy: Enemy = Enemy("Bob")

    def main(self):
        print(self._player.name)
        print(self._enemy.name)


if __name__ == "__main__":
    Main().main()

