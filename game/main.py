import os, sys
sys.path.append(os.path.dirname(sys.argv[0]))


class Character:
    def __init__(self) -> None:
        self.name = ""
        self.stat = None
        self.debuff = None
        self.buff = None

class PowerUp:
    def __init__(self) -> None:
        self.effect = 1.5
        self.description = """Power Up!"""
        print(self.description)


player = Character()