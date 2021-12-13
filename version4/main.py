import random

from copy import deepcopy
from enum import Enum, auto
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, StreamHandler, getLogger

from argparser import args


levels = {
    "debug": DEBUG,
    "info": INFO,
    "warning": WARNING,
    "error": ERROR,
    "critical": CRITICAL
}
level = DEBUG
for key, value in args._get_kwargs():
    if value:
        level = levels.get(key)
logger = getLogger(__name__)
logger.setLevel(level)
logger.addHandler(StreamHandler())


class Quest:
    def __init__(self, name, enemyIdx) -> None:
        self.name = name
        self.enemyIdx = enemyIdx


class Money(int):
    pass


class Status:
    def __init__(self, hitpoint: int, strength: int) -> None:
        self.hitpoint = hitpoint
        self.max_hitpoint = hitpoint
        self.strength = strength
        self.cstrength = strength
        self.debuff = []

    def reset(self, new_):
        print(f"{self.strength}->{new_}")
        self.strength = new_


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

    def execute(self):
        pass

    def get_ability_info(self, player=1):
        pass

    def get_type(self):
        return


class AttackAbility(Ability):
    def execute(self, source: "Player", target: "Player"):
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
    def execute(self, source: "Player", target: "Player"):
        heal = source.job_class.status.hitpoint // self.p
        heal = int(heal)
        if target.job_class.status.max_hitpoint > target.job_class.status.hitpoint + heal:
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

    def execute(self, source: "Player", target: "Player"):
        print(f"+{self}")
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


class JobClass:
    def __init__(self, name, status: Status, abilities: list[Ability]) -> None:
        self.name = name
        self.status = status
        self.abilities = abilities


class Player:
    def __init__(self, name, money, job_class: JobClass) -> None:
        self.name = name
        self.money = money
        self.job_class: JobClass = job_class

    def choose_ability(self, player=1):
        if player:
            for i, ability in enumerate(self.job_class.abilities):
                print(i, ability.name)
            return int(input("> "))

        abilitys = []
        rates = []
        for ability in self.job_class.abilities:
            abilitys.append(ability)
            ability_type = ability.get_type()
            if ability_type == 1:
                rate = 1-(self.job_class.status.hitpoint / self.job_class.status.max_hitpoint)*(1/ability.p)
                if rate <= 0:
                    rate = random.random()
            else:
                rate = random.uniform(abs(1/ability.p-0.5), 1)
            rates.append(rate)
        return self.job_class.abilities.index(random.choices(self.job_class.abilities, rates)[0])

    def exec_ability(self, idx, source, target):
        if isinstance(idx, str):
            if idx.isdigit:
                idx = int(idx)
            else:
                raise ValueError
        return self.job_class.abilities[idx].execute(source, target)

    def message(self, _type, player=1):
        if player:
            msgs = {
                AbilityType.Attack: "{}に{}ダメージをあたえた!",
                AbilityType.Heal: "{}はHP{}回復した!",
                AbilityType.Debuff: "{}に{}の効果!"
            }
        else:
            msgs = {
                AbilityType.Attack: "{}は{}のダメージをうけた!",
                AbilityType.Heal:" {}はHP{}回復した!",
                AbilityType.Debuff: "{}は攻撃力が{}になった!"
            }
        return msgs.get(_type)

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
                del self.job_class.status.debuff[self.job_class.status.debuff.index(debuff)]
                self.job_class.status.reset(_new)


def battle(player: Player, enemy: Player):
    # logger.debug(f"[Start] battle({player.name}, {enemy.name})")
    turn = 0
    print(f"{enemy.name}が現れた!")
    actor = [player, enemy]
    while True:
        turn += 1
        print(f"{turn}: {player.name}のターン! HP:{player.job_class.status.hitpoint}/STR:{player.job_class.status.strength}")
        print(f"DEBUFF:{player.job_class.status.debuff}")
        ability_idx = player.choose_ability()
        ability: Ability = player.job_class.abilities[ability_idx]
        sidx, tidx = ability.get_ability_info()

        print(f"{player.name}の{ability.name}!")
        ability_type = ability.get_type()
        msg = player.message(ability_type)

        d = player.exec_ability(ability_idx, actor[sidx], actor[tidx])
        match ability_type:
            case AbilityType.Heal:
                if d == 0:
                    print("HPが満タンだ!")
                else:
                    print(msg.format(player.name, d))
                    print(f"HP:{player.job_class.status.hitpoint-d}->HP:{player.job_class.status.hitpoint}")
            case AbilityType.Debuff:
                print(msg.format(enemy.name, ability.name))
            case _:
                print(msg.format(enemy.name, d))
        if enemy.job_class.status.hitpoint <= 0:
            print(f"{enemy.name}をたおした!")
            # logger.debug(f"[Finish] battle({player.name}, {enemy.name}) -> 1")
            return 1
        player.turn()
        print(f"{enemy.name}(HP:{enemy.job_class.status.hitpoint})のターン!")
        print(f"DEBUFF:{enemy.job_class.status.debuff}")
        enemy_ability_idx = enemy.choose_ability(0)
        enemy_ability: Ability = enemy.job_class.abilities[enemy_ability_idx]
        enemy_ability_type = enemy_ability.get_type()
        sidx, tidx = enemy_ability.get_ability_info(0)
        enemy_msg = enemy.message(enemy_ability_type, 0)

        print(f"{enemy.name}の{enemy_ability.name}")
        d = enemy.exec_ability(enemy_ability_idx, actor[sidx], actor[tidx])
        match enemy_ability_type:
            case AbilityType.Heal:
                print(enemy_msg.format(enemy.name, d))
            case AbilityType.Attack:
                print(enemy_msg.format(player.name, d))
        if player.job_class.status.hitpoint <= 0:
            print(f"{player.name}はたおされた!")
            # logger.debug(f"[Finish] battle({player.name}, {enemy.name}) -> -1")
            return -1
        enemy.turn()


def game(player: Player):

    slime = Player(
        "スライム",
        Money(300),
        JobClass(
            "スライム",
            Status(1200, 600),
            [AttackAbility("攻撃")]
        )
    )
    dragon = Player(
        "ドラゴン",
        Money(1000),
        JobClass(
            "ドラゴン",
            Status(3000, 900),
            [AttackAbility("攻撃"), AttackAbility("3倍攻撃", 3), HealAbility("回復")]
        )
    )
    debug_enemy = Player(
        "デバッグくん",
        Money(10**10-1),
        JobClass(
            "デバッグくん",
            Status(10**4-1, 200),
            [
                AttackAbility("攻撃"),
                AttackAbility("3倍攻撃", 3),
                HealAbility("2倍回復", 2),
                DebuffAbility("攻撃力ダウン", 0.9, 4)
            ]
        )
    )
    enemies = [slime, dragon]
    quests: list[Quest] = [
        Quest("スライム討伐", 0),
        Quest("ドラゴン討伐", 1)
    ]
    for i, quest in enumerate(quests):
        print(i, quest.name)
    print("-1 デバッグ用")
    quest_idx = int(input("> "))
    if 0 <= quest_idx:
        enemy = enemies[quests[quest_idx].enemyIdx]
    else:
        enemy = debug_enemy
    winner = battle(deepcopy(player), deepcopy(enemy))
    if winner == 1:
        print("You Win!")
        print(f"{enemy.money}Gをかくとく!")
        player.money += enemy.money
        print(f"{player.money-enemy.money}G->{player.money}G")
    else:
        print("You Lose!")
    return player


if __name__ == "__main__":
    # name = input("Enter your name:")
    name = "アリス"
    player = Player(
        name,
        Money(0),
        JobClass(
            "勇者",
            Status(2000, 800),
            [HealAbility("回復"), AttackAbility("攻撃"), AttackAbility("2倍攻撃", 2), DebuffAbility("攻撃力大ダウン", 0.5, 3)]
        )
    )

    while True:
        game(player)
        y = input("Continue? > ")
        if y not in ("y", "Y", "YES", "yes", "Yes"):
            break
    input("Please Press Any Key...")