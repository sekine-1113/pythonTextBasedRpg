from simpleRPG.interface import (
    ABC,
    abstractmethod,
)


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