
class Debuff:
    pass


class Poison(Debuff):
    def __init__(self) -> None:
        self.damage = 5
        self.turn = 3

    def effect(self):
        print("毒の効果!")
        print(self.turn)
        self.turn -= 1
        if self.turn == 0:
            print("毒は消えた!")



class Sleep(Debuff):
    def __init__(self) -> None:
        self.damage = 0
        self.turn = 3

    def effect(self):
        print("眠りの効果!")
        self.turn -= 1
        if self.turn == 0:
            print("眠りは消えた!")


class Player:
    def __init__(self) -> None:
        self.name = "Alice"
        self.debuff = []
        self.hp = 32

    def action(self):
        for debuff in self.debuff:
            if debuff.turn == 0:
                self.debuff.remove(debuff)
                continue
            debuff.effect()


class Enemy:
    def __init__(self) -> None:
        self.name = "Slime"
        self.debuff = []
        self.hp = 16

    def action(self):
        for debuff in self.debuff:
            debuff.effect()



player = Player()
enemy = Enemy()
poison = Poison()
player.debuff.append(poison)

while True:
    player.action()
    if enemy.hp <= 0:
        break
    player.hp -= 8
    if player.hp <= 0:
        break


