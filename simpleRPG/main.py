from abc import ABC, abstractmethod
from tkinter import N


class IStatus(ABC):

    def __init__(self, level: int, HP: int, ATK: int, DEF: int, EXP: int) -> None:
        self.level = level
        self.max_HP = HP
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.EXP = EXP

    def __repr__(self) -> str:
        return (
            f"\n  Lv : {self.level:3}"
            f"\n  HP : {self.HP:3} / {self.max_HP:3}"
            f"\n  ATK: {self.ATK:3}"
            f"\n  DEF: {self.DEF:3}"
            f"\n  EXP: {self.EXP:4}"
        )


class PlayerStatus(IStatus):

    def __init__(self, level: int, HP: int, ATK: int, DEF: int, EXP: int) -> None:
        super().__init__(level, HP, ATK, DEF, EXP)
        self.weapon_ATK = 0

    def get_weapon_information(self, weapon):
        if weapon is None:
            return
        self.weapon_ATK = weapon.ATK

    def __repr__(self) -> str:
        return (
            f"\n  Lv : {self.level:3}"
            f"\n  HP : {self.HP:3} / {self.max_HP:3}"
            f"\n  ATK: {self.ATK:3} + {self.weapon_ATK}"
            f"\n  DEF: {self.DEF:3}"
        )

class EnemyStatus(IStatus):

    def __init__(self, level: int, HP: int, ATK: int, DEF: int, EXP: int) -> None:
        super().__init__(level, HP, ATK, DEF, EXP)

    def __repr__(self) -> str:
        return (
            f"\n  HP : {self.HP:3} / {self.max_HP:3}"
        )


class IActor(ABC):

    def __init__(self, name: str, status: IStatus,) -> None:
        self.name = name
        self.status = status

    @abstractmethod
    def get_instance(self) -> "IActor":
        ...

    @abstractmethod
    def attack(self, target: "IActor") -> int:
        ...

    @abstractmethod
    def receive(self, damage: int) -> None:
        ...

    def is_dead(self) -> bool:
        return self.status.HP <= 0

    def battle_status(self) -> None:
        status = (
            f"Name: {self.name}\n"
            f"Status:\n"
            f"  HP : {self.status.HP} / {self.status.max_HP}\n"
            f"  ATK: {self.status.ATK}"
        )
        print(status)

    def __repr__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Status: {self.status}"
        )


class IWeapon(ABC):

    def __init__(self, name: str, ATK: int) -> None:
        self.name = name
        self.ATK = ATK

    def __repr__(self) -> str:
        return (
            f"\n  Name: {self.name}\n"
            f"  ATK : {self.ATK:3}"
        )


class NullWeapon(IWeapon):

    def __init__(self) -> None:
        super().__init__("None", 0)


class Sword(IWeapon):

    def __init__(self, name: str, ATK: int) -> None:
        super().__init__(name, ATK)


class Player(IActor):

    def __init__(self, name: str, status: PlayerStatus, weapon: IWeapon=None) -> None:
        super().__init__(name, status,)
        self.weapon = weapon
        self.status.get_weapon_information(weapon)

    def get_instance(self) -> "Player":
        return Player(
            name=self.name,
            status=self.status,
            weapon=self.weapon)

    def attack(self, target: IActor) -> None:
        atk = (self.status.ATK + self.weapon.ATK) ** 2
        target.receive(atk)

    def receive(self, damage: int) -> None:
        receive_damage = damage // (self.status.DEF * 3)
        print(self.name, receive_damage)
        self.status.HP -= receive_damage

    def battle_status(self) -> None:
        status = (
            f"Name: {self.name}\n"
            f"Status:\n"
            f"  HP : {self.status.HP} / {self.status.max_HP}\n"
            f"  ATK: {self.status.ATK} + {self.weapon.ATK}"
        )
        print(status)

    def __repr__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Status: {self.status}\n"
            f"Weapon: {self.weapon}"
        )


class Enemy(IActor):

    def __init__(self, name: str, status: EnemyStatus,) -> None:
        super().__init__(name, status,)

    def get_instance(self) -> "Enemy":
        return Enemy(
            name=self.name,
            status=self.status,)

    def attack(self, target: IActor) -> int:
        atk = self.status.ATK ** 2
        target.receive(atk)

    def receive(self, damage: int) -> None:
        receive_damage = damage // (self.status.DEF * 3)
        print(self.name, receive_damage)
        self.status.HP -= receive_damage


if __name__ == "__main__":
    player = Player(
        name="Alice",
        status=PlayerStatus(
            level=1,
            HP=32,
            ATK=12,
            DEF=8,
            EXP=0,
        ),
        weapon=Sword("どうのつるぎ", 2),
    )

    enemy = Enemy(
        name="Enemy",
        status=EnemyStatus(
            level=2,
            HP=32,
            ATK=12,
            DEF=8,
            EXP=2,
        ),
    )

    print("<Player>\n", player, sep="")
    print("<Enemy>\n", enemy, sep="")

    while (not player.is_dead() and not enemy.is_dead()):
        print("="*25)
        print("<Player>")
        player.battle_status()
        print("-"*25)
        print("<Enemy>")
        enemy.battle_status()
        print("="*25)
        player.attack(enemy)
        if enemy.is_dead():
            print("enemy is dead")
            break
        enemy.attack(player)
        if player.is_dead():
            print("player is dead")
            break



