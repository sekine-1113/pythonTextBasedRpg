import random

from settings import Input
from version7.ability import AbilityEntity


class ActorEntity:
    def __init__(self, hitpoint, strength, defence, magicpower, critical) -> None:
        self.hitpoint = hitpoint
        self.max_hitpoint = self.hitpoint
        self.strength = strength
        self.origin_strength = self.strength
        self.defence = defence
        self.origin_defence = self.defence
        self.magicpower = magicpower
        self.origin_magicpower = self.magicpower
        self.critical = critical
        self.abilities = None
        self.enemy_ai = None

    def set_enemy_ai(self, ai) -> None:
        self.enemy_ai = ai

    def set_abilities(self, abilities) -> None:
        self.abilities = abilities

    def ability_select(self) -> int:
        for i, ability in enumerate(self.abilities, 1):
            print(i, ability.name)
        print(0, "リタイア")
        return Input.integer_with_range(_max=len(self.abilities))-1

    def get_ability(self, idx) -> AbilityEntity:
        return self.abilities[idx]

    def execute(self, idx: int) -> int:
        ability: AbilityEntity = self.get_ability(idx)
        if not ability.can_use():
            return -1
        ability.count -= 1
        critical = self.critical >= random.randint(0, 100) >= 0
        if critical:
            print("Critical!")
        if ability.type_ == 0:  # 攻撃
            damage = ability.fixed_value + (ability.value/10) * self.strength
            damage += damage * 0.2 * critical
            return damage
        elif ability.type_ == 1:  # 回復
            heal = ability.fixed_value + (ability.value/10) * self.magicpower
            heal += heal * 0.2 * critical
            return heal
        elif ability.type_ == 2:
            damage = ability.fixed_value + (ability.value/10) * self.strength
            damage += damage * 0.2 * critical
            return damage
        return 0

    def take_damage(self, damage: int) -> int:
        self.hitpoint -= int(damage - self.defence/4)
        return int(damage - self.defence/4)

    def take_heal(self, heal: int) -> int:
        if self.hitpoint + heal > self.max_hitpoint:
            heal = self.max_hitpoint - self.hitpoint
        self.hitpoint += heal
        return heal

    def is_dead(self) -> bool:
        return self.hitpoint <= 0


