
class Stats:
    def __init__(self, hit_point, magic_power, strength, defence) -> None:
        self.hit_point = hit_point
        self.max_hit_point = hit_point
        self.magic_power = magic_power
        self.strength = strength
        self.defence = defence


class ActorName(str):
    pass


class Weapon:
    def __init__(self, name, attack_power) -> None:
        self.name = name
        self.attack_power = attack_power

    def __repr__(self) -> str:
        return f"'{self.name}'"


class Item:
    pass


class Inventory:
    pass


class Actor:
    def __init__(self, name: ActorName, stats: Stats, inventory: Inventory, weapon: Weapon) -> None:
        self.name = name
        self.stats = stats
        self.inventory = inventory
        self.weapon = weapon


    def display_stats(self):
        print(f"{self.name}")
        print(f"HP : {self.stats.hit_point:4} / {self.stats.max_hit_point:4}")
        print(f"MP : {self.stats.magic_power:4}")
        print(f"STR: {self.stats.strength:4} + {self.weapon.attack_power}")
        print(f"DEF: {self.stats.defence:4}")
        print(f"Weapn: {self.weapon}")


    def set_item(self, item):
        pass



if __name__ == "__main__":
    actor = Actor(
        ActorName("Alice"),
        Stats(300, 0, 100, 50),
        0,
        Weapon("どうのつるぎ", 10)
    )
    actor.display_stats()
    actor.stats.level = 1
    print(f"レベル{actor.stats.level:4}")
    print(f"HP{actor.stats.hit_point:8}")
    print(f"MP{actor.stats.magic_power:8}")
