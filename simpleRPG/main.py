

class Actor:
    def __init__(self, name, hp, power, exp, is_player) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.exp = exp
        self.is_player = is_player

    def show(self):
        print(f"Name: {self.name}")
        print(f"HP : {self.hp:3}")
        if self.is_player:
            print(f"STR: {self.power:3}")
            print(f"EXP: {self.exp:3}")

    def __repr__(self) -> str:
        return self.name


def main():
    player = Actor("Player", 30, 8, 0, True)
    enemy = Actor("Enemy", 24, 6, 4, False)
    print("Welcom to SimpleRPG!")
    gameloop = input("[1] Start [0] Exit > ")

    if (not gameloop):
        print("Bye!")
        return

    player.show()
    enemy.show()


main()

