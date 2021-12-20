from copy import deepcopy

from version4.actor import Actor, Player, Enemy
from version4.ability import AbilityType, Ability, AttackAbility, HealAbility, DebuffAbility


def set_logger(logger_name=None):
    from logging import (
        CRITICAL, DEBUG, ERROR, INFO, WARNING, StreamHandler, getLogger)
    from .argparser import args

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
    if logger_name is None:
        logger_name = __name__
    logger = getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(StreamHandler())
    return logger


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


class JobClass:
    def __init__(self, name, status: Status,
                    abilities: list[Ability]) -> None:
        self.name = name
        self.status = status
        self.abilities = abilities


def battle(player: Actor, enemy: Actor):
    turn = 0
    print(f"{enemy.name}が現れた!")

    actors = [player, enemy]
    while True:
        turn += 1
        print(f"{turn}: {player.name}({player.job_class.name})のターン! ")
        print(f"HP:{player.job_class.status.hitpoint}/STR:{player.job_class.status.strength}")
        print(f"DEBUFF:{player.job_class.status.debuff}")
        ability_idx = player.choose_ability()
        ability: Ability = player.job_class.abilities[ability_idx]
        sidx, tidx = ability.get_ability_info()
        print(f"{player.name}の{ability.name}!")
        ability_type = ability.get_type()
        msg = player.message(ability_type)

        d = player.exec_ability(ability_idx, actors[sidx], actors[tidx])
        match ability_type:
            case AbilityType.ATTACK:
                print(msg.format(enemy.name, d))
            case AbilityType.HEAL:
                if d == 0:
                    print("HPが満タンだ!")
                else:
                    print(msg.format(player.name, d))
                    print(f"HP:{player.job_class.status.hitpoint-d}->HP:{player.job_class.status.hitpoint}")
            case AbilityType.DEBUFF:
                print(msg.format(enemy.name, ability.name))
            case _:
                pass
        if enemy.job_class.status.hitpoint <= 0:
            print(f"{enemy.name}をたおした!")
            # logger.debug(f"[Finish] battle({player.name}, {enemy.name}) -> 1")
            return 1
        player.turn()
        print(f"{enemy.name}(HP:{enemy.job_class.status.hitpoint})のターン!")
        print(f"DEBUFF:{enemy.job_class.status.debuff}")
        enemy_ability_idx = enemy.choose_ability()
        enemy_ability: Ability = enemy.job_class.abilities[enemy_ability_idx]
        enemy_ability_type = enemy_ability.get_type()
        sidx, tidx = enemy_ability.get_ability_info(0)
        enemy_msg = enemy.message(enemy_ability_type)
        print(f"{enemy.name}の{enemy_ability.name}")
        d = enemy.exec_ability(enemy_ability_idx, actors[sidx], actors[tidx])
        match enemy_ability_type:
            case AbilityType.ATTACK:
                print(enemy_msg.format(player.name, d))
            case AbilityType.HEAL:
                print(enemy_msg.format(enemy.name, d))
            case AbilityType.DEBUFF:
                print(enemy_msg.format(player.name, d))
            case _:
                pass
        if player.job_class.status.hitpoint <= 0:
            print(f"{player.name}はたおされた!")
            return -1
        enemy.turn()


def select_quest(player: Player):

    slime = Enemy(
        "スライム",
        Money(300),
        JobClass(
            "スライム",
            Status(1200, 600),
            [AttackAbility("攻撃")]
        )
    )
    dragon = Enemy(
        "ドラゴン",
        Money(1000),
        JobClass(
            "ドラゴン",
            Status(3000, 900),
            [AttackAbility("攻撃"), AttackAbility("3倍攻撃", 3), HealAbility("回復")]
        )
    )
    debug_enemy = Enemy(
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
        print(f"{enemy.exp}EXPをかくとく!")
        player.exp += enemy.exp
        print(f"{enemy.money}Gをかくとく!")
        player.money += enemy.money
        print(f"{player.money-enemy.money}G->{player.money}G")
    else:
        print("You Lose!")
    return player


if __name__ == "__main__":
    # いつかつくる
    # name = input("Enter your name:")

    name = "アリス"
    player = Player(
        name,
        Money(0),
        JobClass(
            "勇者",
            Status(2000, 800),
            [
                HealAbility("回復"),
                AttackAbility("攻撃"),
                AttackAbility("2倍攻撃", 2),
                DebuffAbility("攻撃力大ダウン", 0.5, 3)
            ]
        )
    )

    while True:
        select_quest(player)
        y = input("Continue? > ")
        if y not in ("y", "Y", "YES", "yes", "Yes"):
            break
    input("Please Press Any Key...")