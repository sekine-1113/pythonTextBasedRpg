import os, sys
sys.path.append(os.path.dirname(sys.argv[0]))


from myfunc import *



class Weapon:
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power
        self.damage_up = 0.01

    def __repr__(self) -> str:
        return self.name


class Sword(Weapon):
    def __init__(self, name, power) -> None:
        super().__init__(name, power)


class Player:
    def __init__(self, health, power, weapon) -> None:
        self.name = "アリス"
        self.weapon = weapon
        self.health = health
        self.power = power

    def add_weapon_power(self):
        return self.power + self.weapon.power

    def attack(self, target):
        power = self.add_weapon_power()
        power = int(power * (1+self.weapon.damage_up))
        target.health -= power


class Enemy:
    def __init__(self, health, power) -> None:
        self.name = "ゴブリン"
        self.weapon = Weapon("なし", 0)
        self.health = health
        self.power = power

    def add_weapon_power(self):
        return self.power + self.weapon.power

    def attack(self, target: Player):
        power = self.add_weapon_power()
        power = int(power * (1+self.weapon.damage_up))
        target.health -= power



player = Player(30, 10, Sword("どうのつるぎ", 5))
enemy = Enemy(25, 12)

while player.health > 0:
    print(player.name, player.health)
    player.attack(enemy)
    print(enemy.name, enemy.health)
    enemy.attack(player)

print(player.name, player.health)
print(enemy.name, enemy.health)