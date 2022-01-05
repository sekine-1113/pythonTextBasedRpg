class AbilityEntity:
    def __init__(self, name, description, count, target, type_, fixed_value, value) -> None:
        self.name = name
        self.description = description
        self.count = count
        self.target = target
        self.type_ = type_
        self.fixed_value = fixed_value
        self.value = value

    def can_use(self) -> bool:
        return self.count > 0

    def __str__(self) -> str:
        return f"{self.name} {self.count}"

