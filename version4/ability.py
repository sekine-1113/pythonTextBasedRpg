from __future__ import annotations
from enum import Enum, auto
from typing import TYPE_CHECKING




if TYPE_CHECKING:
    from version4.actor import Actor


class AbilityType(Enum):
    Attack = auto()
    Heal = auto()
    Debuff = auto()


class Ability:
    def __init__(self, name, p=1, turn=0) -> None:
        self.name = name
        self.p = p
        self._type = 0
        self.turn = turn

    def execute(self, source: Actor, target: Actor):
        pass

    def get_ability_info(self, player=1):
        pass

    def get_type(self):
        pass


class AttackAbility(Ability):
    def execute(self, source: Actor, target: Actor):
        damage = source.job_class.status.strength * self.p
        damage = int(damage)
        target.job_class.status.hitpoint -= damage
        return damage

    def get_ability_info(self, player=1):
        if player:
            return [0, 1]
        else:
            return [1, 0]

    def get_type(self):
        return AbilityType.Attack


class HealAbility(Ability):
    def execute(self, source: Actor, target: Actor):
        heal = source.job_class.status.hitpoint // self.p
        heal = int(heal)
        if target.job_class.status.max_hitpoint > (target.job_class.status.hitpoint + heal):
            target.job_class.status.hitpoint += heal
        else:
            heal = target.job_class.status.max_hitpoint - target.job_class.status.hitpoint
            target.job_class.status.hitpoint = target.job_class.status.max_hitpoint
        return heal

    def get_type(self):
        return AbilityType.Heal

    def get_ability_info(self, player=1):
        if player:
            return [0, 0]
        else:
            return [1, 1]


class DebuffAbility(Ability):
    def __init__(self, name, p=1, turn=0) -> None:
        super().__init__(name, p=p, turn=turn)
        self.eturn = turn  # effective turn

    def __iter__(self):
        return self

    def __next__(self):
        if self.turn <= 1:
            raise StopIteration()
        self.turn -= 1

    def execute(self, source: Actor, target: Actor):
        old = target.job_class.status.strength
        target.job_class.status.strength *= self.p
        target.job_class.status.strength = int(target.job_class.status.strength)
        print(f"{old}->{target.job_class.status.strength}")
        target.job_class.status.debuff.append(
            DebuffAbility(self.name, self.p, self.eturn)
        )
        return int(target.job_class.status.strength)

    def get_type(self):
        return AbilityType.Debuff

    def get_ability_info(self, player=1):
        if player:
            return [1, 1]
        else:
            return [0, 0]

    def __repr__(self) -> str:
        return f"{self.name} @{self.turn}"
