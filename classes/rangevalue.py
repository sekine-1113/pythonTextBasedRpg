class RangeValue:
    """ranged value
    - _min: minimam value
    - _max: maxumam value
    - current: current value
    """
    def __init__(self, current: int, _min: int=0, _max: int=99999) -> None:
        self.min = _min
        self.max = _max
        self.current = current if _min <= current <= _max else _max

    def change_current(self, value: int) -> None:
        if self.min <= value <= self.max:
            self.current = value
        return self

    def change_min(self, value: int, _jugde: bool=False) -> None:
        if _jugde: value = max(self.min, value)
        self.min = value
        return self

    def change_max(self, value: int, _jugde: bool=False) -> None:
        if _jugde: value = min(self.max, value)
        self.max = value
        return self

    def decrease_current(self, value: int) -> None:
        self.current -= value
        if self.current < self.min: self.current = self.min
        return self

    def increase_current(self, value: int) -> None:
        self.current += value
        if self.current > self.max: self.current = self.max
        return self

    def increase_max(self, value: int) -> None:
        self.max += value
        return self

    def increase(self, value: int) -> None:
        self.increase_max(value)
        self.increase_current(value)
        return self

    def reset(self) -> None:
        self.current = self.max
        return self

    def rate(self) -> float:
        return round(self.current / self.max * 100)

    def rate_change(self, value: int) -> None:
        self.current = round(self.current * (value / 100))
        return self

    def __repr__(self) -> str:
        return f"[{self.min},{self.current},{self.max}]"

