
class Spell:
    def __init__(self, name, cost, damage) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage


if __name__ == "__main__":
    fire = Spell("ファイア", 2, 20)
    assert fire.name == "ファイア"
    assert fire.cost == 2
    assert fire.damage == 20