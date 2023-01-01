from games.cui.textbasedrpg.alpha.interface._varstat import _VariableStat


class VariableStat(_VariableStat):

    def __init__(self, value: int) -> None:
        assert isinstance(value, int)
        self.value: int = value
        self.max_value: int = value
        self.min_value: int = 0

    def add(self, value: int) -> None:
        assert isinstance(value, int)
        self.value += value
        self.max_value = self.value

    def decrease(self, value: int) -> None:
        assert isinstance(value, int)
        self.value = max(self.value-value, self.min_value)

    def recover(self, value: int) -> None:
        assert isinstance(value, int)
        self.value = min(self.value+value, self.max_value)

    def restore(self) -> None:
        self.value = self.max_value