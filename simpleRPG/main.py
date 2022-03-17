from copy import deepcopy

# from simpleRPG import (
#     os,
#     sys,
# )
from simpleRPG import (
    no_random,
    random,
)
from simpleRPG.interface.actor import IActor
from simpleRPG.interface.status import IStatus
from simpleRPG.interface.weapon import IWeapon
from simpleRPG.io import (
    integer,
    output,
)
from simpleRPG.io.color import (
    Color,
    BackGroundColor,
)
from simpleRPG.io.file import (
    get_path,
    load
)


class PlayerStatus(IStatus):

    def __init__(self, level: int, HP: int, ATK: int, DEF: int, EXP: int) -> None:
        super().__init__(
            level,
            HP,
            ATK,
            DEF,
            EXP,
        )
        self.weapon_ATK = 0

    def set_weapon_information(self, weapon: IWeapon) -> None:
        if weapon is None:
            return
        self.weapon_ATK = weapon.ATK

    def __repr__(self) -> str:
        return (
            f"\n  Lv : {self.level:3}"
            f"\n  HP : {self.HP:3} / {self.max_HP:3}"
            f"\n  ATK: {self.ATK:3} + {self.weapon_ATK}"
            f"\n  DEF: {self.DEF:3}"
            f"\n  EXP: {self.EXP:4}"
        )


class EnemyStatus(IStatus):

    def __init__(self, level: int, HP: int, ATK: int, DEF: int, EXP: int) -> None:
        super().__init__(
            level,
            HP,
            ATK,
            DEF,
            EXP,
        )

    def __repr__(self) -> str:
        return (
            f"\n  HP : {self.HP:3} / {self.max_HP:3}"
        )


class Weapon(IWeapon):

    def __init__(self, id_:int, name: str, ATK: int) -> None:
        super().__init__(id_, name, ATK)


class Player(IActor):

    def __init__(self, name: str, status: PlayerStatus, weapon: IWeapon=None, random_function: random.randint=random.randint) -> None:
        super().__init__(
            name,
            status,
            random_function,
        )
        self.weapon = weapon
        self.status.set_weapon_information(weapon)

    def set_level(self, level: int) -> None:
        self.status.level = level

    def add_exp(self, exp: int) -> None:
        self.status.EXP += exp

    def can_level_up(self) -> None:
        level_data = {
            1: 0,
            2: 8,
            3: 16,
            4: 24,
            5: 40,
        }
        diff_level = max([lv for lv, exp in level_data.items() if exp > self.status.EXP])
        return diff_level - self.status.level >= 1

    def level_up(self) -> None:
        output("Level Up!")
        self.set_level(self.status.level + 1)
        old_HP = self.status.HP
        add_HP = self._random(2, 4)
        self.status.max_HP += add_HP
        self.status.HP += add_HP
        new_HP = self.status.HP
        output(f"HP : {old_HP} -> {new_HP} (+{add_HP})")
        old_ATK = self.status.ATK
        add_ATK = self._random(2, 3)
        self.status.ATK += add_ATK
        new_ATK = self.status.ATK
        output(f"ATK: {old_ATK} -> {new_ATK} (+{add_ATK})")
        old_DEF = self.status.DEF
        add_DEF = self._random(1, 2)
        self.status.DEF += add_DEF
        new_DEF = self.status.DEF
        output(f"DEF: {old_DEF} -> {new_DEF} (+{add_DEF})")

    def set_weapon(self, weapon: IWeapon) -> None:
        self.weapon = weapon
        self.status.set_weapon_information(self.weapon)

    def get_instance(self) -> "Player":
        return deepcopy(self)

    def attack(self, target: IActor) -> None:
        damage = (self.status.ATK + self.weapon.ATK) ** 2 + self._random(0, 100)
        target.receive(damage)

    def receive(self, damage: int) -> None:
        receive_damage = int(damage / (self.status.DEF * 3))
        output(self.name, receive_damage)
        self.status.HP -= receive_damage

    def show_battle_status(self) -> None:
        status = (
            f"Name: {self.name}\n"
            f"Status:\n"
            f"  HP : {self.status.HP} / {self.status.max_HP}\n"
            f"  ATK: {self.status.ATK} + {self.weapon.ATK}"
        )
        output(status)

    def __repr__(self) -> str:
        return (
            f"{'='*25}\n"
            f"Name: {self.name}\n"
            f"Status: {self.status}\n"
            f"Weapon: \n{self.weapon}"
        )


class Enemy(IActor):

    def __init__(self, name: str, status: EnemyStatus, random_function: random.randint=random.randint) -> None:
        super().__init__(
            name,
            status,
            random_function,
        )

    def get_instance(self) -> "Enemy":
        return deepcopy(self)

    def attack(self, target: IActor) -> int:
        damage = self.status.ATK ** 2 + self._random(0, 100)
        target.receive(damage)

    def receive(self, damage: int) -> None:
        receive_damage = int(damage / (self.status.DEF * 3))
        output(self.name, receive_damage)
        self.status.HP -= receive_damage


if __name__ == "__main__":
    weapon_data = [
        {
            "id": 0,
            "name": "None",
            "ATK": 0,
        },
        {
            "id": 1,
            "name": "どうのつるぎ",
            "ATK": 4,
        },
        {
            "id": 2,
            "name": "はがねのつるぎ",
            "ATK": 8,
        },
    ]

    weapon_instances = [
        Weapon(weapon.get("id"), weapon.get("name"), weapon.get("ATK"))
        for weapon in weapon_data
    ]

    player_data = {
        "name": "Alice",
        "status": {
            "level": 1,
            "HP": 32,
            "ATK": 12,
            "DEF": 8,
            "EXP": 0,
        },
        "weapon": { "id": 1, },
    }

    player = Player(
        name=player_data.get("name"),
        status=PlayerStatus(
            level=player_data.get("status").get("level"),
            HP=player_data.get("status").get("HP"),
            ATK=player_data.get("status").get("ATK"),
            DEF=player_data.get("status").get("DEF"),
            EXP=player_data.get("status").get("EXP"),
        ),
        weapon=weapon_instances[player_data.get("weapon").get("id")],
    )

    enemy_data = {
        "id": 0,
        "name": "Slime",
        "status": {
            "level": 2,
            "HP": 24,
            "ATK": 8,
            "DEF": 6,
            "EXP": 4,
        },
    }

    enemy = Enemy(
        name=enemy_data.get("name"),
        status=EnemyStatus(
            level=enemy_data.get("status").get("level"),
            HP=enemy_data.get("status").get("HP"),
            ATK=enemy_data.get("status").get("ATK"),
            DEF=enemy_data.get("status").get("DEF"),
            EXP=enemy_data.get("status").get("EXP"),
        ),
    )

    output(player)
    output(enemy)

    cp_player = player.get_instance()
    player = player.get_instance()

    while (not player.is_dead() and not enemy.is_dead()):
        output("="*25)
        player.show_battle_status()
        output("-"*25)
        enemy.show_battle_status()
        output("="*25)

        player.attack(enemy)
        if enemy.is_dead():
            output("enemy is dead")
            break

        enemy.attack(player)
        if player.is_dead():
            output("player is dead")
            break

    player = cp_player.get_instance()
    player.set_weapon(weapon_instances[2])
    output(player)

