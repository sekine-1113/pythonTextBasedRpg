from games.cui.textbasedrpg.alpha.core import ABC, abstractmethod


class _VariableStat(ABC):

    @abstractmethod
    def add(self, value: int) -> None: ...

    @abstractmethod
    def decrease(self, value: int) -> None: ...

    @abstractmethod
    def recover(self, value: int) -> None: ...

    @abstractmethod
    def restore(self) -> None: ...