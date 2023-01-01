
import random



class _Actor:
    def __init__(self, attack, defense) -> None:
        self.attack = attack
        self.defense = defense


class Actor(_Actor):
    def __init__(self, attack, defense) -> None:
        super().__init__(attack, defense)


class Damage:
    def __init__(self, value) -> None:
        self.value = value


class DamageCulcrator:
    def calc(self, sorce, target) -> Damage:

        base_damage = int(sorce.attack * 2 / (1 + (target.defense * 4)))
        append_max_damage = base_damage // 16
        append_damage = random.randint(0, append_max_damage)
        return Damage(base_damage + append_damage)



base_attack_power = 120000
base_damage = int(base_attack_power / 10)
bonus_damage = int(base_damage / 10)

max_ = 0
min_ = float("inf")
for _ in range(10000):
    damage = (base_damage + random.randint(0, bonus_damage)) * 10
    if max_ < damage:
        max_ = damage
    if min_ > damage:
        min_ = damage

print(min_, max_)