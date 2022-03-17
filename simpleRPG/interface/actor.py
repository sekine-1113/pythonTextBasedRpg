from simpleRPG.interface import (
    ABC,
    abstractmethod,
    random,
)
from simpleRPG.interface.status import IStatus


class IActor(ABC):

    def __init__(self, name: str, status: IStatus, money: int, random_function: random.randint=random.randint) -> None:
        self.name = name
        self.status = status
        self.money = money
        self._random = random_function

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
            f"Status: {self.status}"
        )