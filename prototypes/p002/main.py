
class FieldEffect:
    def __init__(self) -> None:
        self.name = ""

    def effect(self):
        self.name = "SimpleField"
        print(self.name)
        return True


class Battle:
    def __init__(self, fields: list[FieldEffect]) -> None:
        self.fields: list[FieldEffect] = fields

    def run(self):
        for field in self.fields:
            print(field.effect())

Battle([FieldEffect()]).run()