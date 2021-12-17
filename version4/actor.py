from __future__ import annotations
import random
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from version4.ability import AbilityType, DebuffAbility
    from version4.main import JobClass

import version4.ability

AbilityType = version4.ability.AbilityType


class Actor:
    def __init__(self, name, money, job_class: JobClass) -> None:
        self.name = name
        self.money = money
        self.exp = 0
        self.job_class = job_class

    def choose_ability(self):
        ...

    def exec_ability(self, idx: int|str, source: Actor, target: Actor):
        if isinstance(idx, str):
            if idx.isdigit:
                idx = int(idx)
            else:
                raise ValueError
        return self.job_class.abilities[idx].execute(source, target)

    def message(self, _type: AbilityType):
        ...

    def turn(self):
        debuff: DebuffAbility
        debuffs = list()
        debuffs.extend(self.job_class.status.debuff)
        for debuff in debuffs:
            try:
                next(debuff)
            except StopIteration:
                print(f"-{debuff}")
                _new = int(self.job_class.status.strength/debuff.p)
                del self.job_class.status.debuff[
                    self.job_class.status.debuff.index(debuff)]
                self.job_class.status.reset(_new)


class Player(Actor):
    def __init__(self, name, money, job_class: JobClass) -> None:
        super().__init__(name, money, job_class)

    def choose_ability(self):
        for i, ability in enumerate(self.job_class.abilities):
            print(i, ability.name)
        return int(input("> "))

    def message(self, _type: AbilityType):
        msgs = {
            AbilityType.ATTACK: "{}に{}ダメージをあたえた!",
            AbilityType.HEAL: "{}はHP{}回復した!",
            AbilityType.DEBUFF: "{}に{}の効果!"
        }
        return msgs.get(_type)


class Enemy(Actor):
    def __init__(self, name, money, job_class: JobClass) -> None:
        super().__init__(name, money, job_class)
        self.exp = 30

    def choose_ability(self):
        abilitys = []
        rates = []
        for ability in self.job_class.abilities:
            abilitys.append(ability)
            ability_type = ability.get_type()
            if ability_type == 1:
                rate = 1-(self.job_class.status.hitpoint \
                        / self.job_class.status.max_hitpoint) \
                        * (1/ability.p)
                if rate < 0:
                    rate = random.random()
                elif rate == 0:
                    rate = 1/100
            else:
                rate = random.uniform(abs(1/ability.p-0.5), 1)
            rates.append(rate)
        return self.job_class.abilities.index(
                    random.choices(self.job_class.abilities, rates)[0])

    def message(self, _type):
        msgs = {
            AbilityType.ATTACK: "{}は{}のダメージをうけた!",
            AbilityType.HEAL: "{}はHP{}回復した!",
            AbilityType.DEBUFF: "{}は攻撃力が{}になった!"
        }
        return msgs.get(_type)