class Weapon:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Weapon: <'{self.name}'>"


class NoWeapon:
    def __init__(self) -> None:
        self.name = "None"

    def __repr__(self) -> str:
        return f"<{self.name}>"

DEFAULT_WEAPON = NoWeapon()

class Player:
    def __init__(self, name, weapon=DEFAULT_WEAPON, stats=None) -> None:
        self.name = name
        self.weapon = weapon
        self.stats = stats

    def equip_weapon(self, weapon):
        return Player(self.name, weapon=weapon, stats=self.stats)

    def unequip_weapon(self):
        return Player(self.name, weapon=DEFAULT_WEAPON, stats=self.stats)


p = Player("アリス")
print(p.weapon)
p = p.equip_weapon(Weapon("つよい武器"))
print(p.weapon)
p = p.unequip_weapon()
print(p.weapon)
