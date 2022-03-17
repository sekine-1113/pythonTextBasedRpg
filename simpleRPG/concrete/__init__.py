from simpleRPG import deepcopy
from simpleRPG.interface import random
from simpleRPG.interface.actor import IActor
from simpleRPG.interface.status import IStatus
from simpleRPG.interface.weapon import IWeapon


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
            f"\n  EXP: {self.EXP:3}"
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

    def __init__(
            self,
            name: str,
            status: PlayerStatus,
            money: int,
            random_function: random.randint=random.randint
        ) -> None:
        super().__init__(
            name,
            status,
            money,
            random_function,
        )


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
        print("Level Up!")
        self.set_level(self.status.level + 1)
        old_HP = self.status.HP
        add_HP = self._random(2, 4)
        self.status.max_HP += add_HP
        self.status.HP += add_HP
        new_HP = self.status.HP
        print(f"HP : {old_HP} -> {new_HP} (+{add_HP})")
        old_ATK = self.status.ATK
        add_ATK = self._random(2, 3)
        self.status.ATK += add_ATK
        new_ATK = self.status.ATK
        print(f"ATK: {old_ATK} -> {new_ATK} (+{add_ATK})")
        old_DEF = self.status.DEF
        add_DEF = self._random(1, 2)
        self.status.DEF += add_DEF
        new_DEF = self.status.DEF
        print(f"DEF: {old_DEF} -> {new_DEF} (+{add_DEF})")

    def get_instance(self) -> "Player":
        return deepcopy(self)

    def attack(self, target: IActor) -> None:
        damage = self.status.ATK ** 2 + self._random(0, 100)
        target.receive(damage)

    def receive(self, damage: int) -> None:
        receive_damage = int(damage / (self.status.DEF * 3))
        print(self.name, receive_damage)
        self.status.HP -= receive_damage

    def show_battle_status(self) -> None:
        status = (
            f"Name: {self.name}\n"
            f"Status:\n"
            f"  HP : {self.status.HP} / {self.status.max_HP}\n"
            f"  ATK: {self.status.ATK}"
        )
        print(status)

    def __repr__(self) -> str:
        return (
            f"{'='*25}\n"
            f"Name: {self.name}\n"
            f"Status: {self.status}\n"
            f"Money: {self.money:3}"
        )


class Enemy(IActor):

    def __init__(self, name: str, status: EnemyStatus, money: int, random_function: random.randint=random.randint) -> None:
        super().__init__(
            name,
            status,
            money,
            random_function,
        )

    def get_instance(self) -> "Enemy":
        return deepcopy(self)

    def attack(self, target: IActor) -> int:
        damage = self.status.ATK ** 2 + self._random(0, 100)
        target.receive(damage)

    def receive(self, damage: int) -> None:
        receive_damage = int(damage / (self.status.DEF * 3))
        print(self.name, receive_damage)
        self.status.HP -= receive_damage