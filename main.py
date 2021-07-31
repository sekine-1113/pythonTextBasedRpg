import os, sys
sys.path.append(os.path.dirname(sys.argv[0]))


class IActor:
    def __init__(self, name, hitpoint, strength) -> None:
        self.name = name
        self.hitpoint = hitpoint
        self.strength = strength

    def attack(self):
        pass


class Actor:
    def __init__(self, name, hitpoint, strength) -> None:
        self.name = name
        self.hitpoint = hitpoint
        self.strength = strength
        self.skill = None

    def attack(self, target: IActor):
        damage = int(self.strength * 1.2)
        print(self.name,"damage:", damage)
        target.hitpoint -= damage

    def choose_skill(self):
        if self.skill is None:
            return 0
        for i, v in enumerate(self.skill):
            print(i, v)
        n = int(input(">> "))
        return n


class Wizard(Actor):
    def __init__(self, hitpoint, strength) -> None:
        super().__init__("Wizard", hitpoint, strength)
        self.skill = ["Fire", "Heal"]


class Fighter(Actor):
    def __init__(self,  hitpoint, strength) -> None:
        super().__init__("Fighter", hitpoint, strength)
        self.skill = ["Kill"]


class Goblin(Actor):
    def __init__(self, hitpoint, strength) -> None:
        super().__init__("Goblin", hitpoint, strength)


def main():
    print("Choice your role")
    roles = {
        1: Wizard,
        2: Fighter,
    }
    stats = {
        1: {"hp":1200, "str":300},
        2: {"hp":1500, "str":400}
    }
    for k, v in roles.items():
        print(k, v.__name__)
    i = int(input(">> "))
    player: Actor = roles[i](stats[i]["hp"], stats[i]["str"])
    goblin = Goblin(800, 120)
    print(f"{goblin.name}", "があらわれた")
    while True:
        player.attack(goblin)
        if goblin.hitpoint <= 0:
            print("Killed!")
            break
        goblin.attack(player)
        if player.hitpoint <= 0:
            print("Dead!")
            break



main()