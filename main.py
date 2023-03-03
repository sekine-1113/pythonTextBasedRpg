from abc import ABC, abstractmethod

class Stat:
    def __init__(self, value):
        self.value = max(0, value)

    def update(self, amount):
        self.value = max(0, self.value - amount)


class HP(Stat):
    pass

class Attack(Stat):
    pass



class Actor:
    def __init__(self, name, hp, atk) -> None:
        self.name = name
        self.hp = hp
        self.atk = atk

    def print_status(self) -> None:
        print(f"{self.name} HP:{self.hp.value} ATK:{self.atk.value}")

    def is_dead(self) -> bool:
        return self.hp.value <= 0

    def attack(self, target):
        self.show_attack_message(target, self.atk.value)
        target.hp.update(self.atk.value)

    def show_attack_message(self):
        pass

    def clone(self):
        pass




class Player(Actor):
    def __init__(self, name, hp, atk) -> None:
        super().__init__(name, hp, atk)

    def show_attack_message(self, target, dmg):
        print(self.name, "の", "こうげき")
        print(target.name, "に", dmg, "ダメージを与えた!")

    def clone(self) -> "Player":
        return Player(self.name, self.hp, self.atk)

    def on_turn(self, target):
        command = int(input("[1]Attack [0]Run\n>"))
        match command:
            case 0:
                print("にげた!")
                return False
            case 1:
                self.attack(target)
        return True


class Enemy(Actor):
    def __init__(self, name, hp, atk) -> None:
        super().__init__(name, hp, atk)

    def show_attack_message(self, target, dmg):
        print(self.name, "の", "こうげき")
        print(target.name, "は", dmg, "ダメージを受けた!")

    def clone(self) -> "Enemy":
        return Enemy(self.name, self.hp, self.atk)

    def on_turn(self, target):
        command = 1
        match command:
            case 0:
                print("にげだした!")
                return False
            case 1:
                self.attack(target)
        return True


if __name__ == "__main__":

    player = Player("アリス", HP(300), Attack(120))
    enemy = Enemy("スライム", HP(180), Attack(90))

    clone_player = player.clone()
    clone_enemy = enemy.clone()

    print(enemy.name,"が現れた!")

    player.print_status()
    enemy.print_status()


    while True:

        result = player.on_turn(enemy)
        if not result:
            break

        if enemy.is_dead():
            print(enemy.name,"を倒した!")
            break

        result = enemy.on_turn(player)
        if not result:
            break

        if player.is_dead():
            print(player.name,"は死んでしまった...")
            break

        player.print_status()
        enemy.print_status()


    player.print_status()
    enemy.print_status()

    player = clone_player
    enemy = clone_enemy