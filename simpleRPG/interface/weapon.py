from simpleRPG.interface import (
    ABC,
    abstractmethod,
)


class IWeapon(ABC):

    def __init__(self, id_:int, name: str, ATK: int) -> None:
        self.id_ = id_
        self.name = name
        self.ATK = ATK

    def show_information(self) -> str:
        return (
            f"Name: {self.name} "
            f"ATK : {self.ATK:3}"
        )

    def __repr__(self) -> str:
        return (
            f"  Name: {self.name}\n"
            f"  ATK :{self.ATK:3}"
        )