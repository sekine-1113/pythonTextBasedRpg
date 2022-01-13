from abc import ABC, abstractmethod


class IWeapon(ABC):
    @abstractmethod
    def attack(self):
        ...


class NormalWeapon(IWeapon):
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power

    def attack(self):
        return self.power



class Player:
    def __init__(self, name, hp, strength, weapon:IWeapon) -> None:
        self.name = name
        self.hp = hp
        self.strength = strength
        self.weapon = weapon

    def attack(self):
        return self.strength

    def total_attack(self):
        return self.strength + self.weapon.attack()


power = Player(
        "アリス",
        3000,
        800,
        NormalWeapon("どうのつるぎ", 200)
    ).total_attack()
print(power)