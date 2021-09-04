from abc import ABC, abstractmethod


class Role(ABC):

    def __init__(self, level) -> None:
        self.name = ""
        self._id = -1
        self.level = level
        self.hitpoint = -1
        self.magicpower = -1
        self.strength = -1
        self.defence = -1
        self.wisdom = -1
        self.exp = 0


    @abstractmethod
    def init(self) -> None:
        pass


    def level_up(self):
        self.level += 1
        self.init()


    def show(self):
        print(f"Job: {self.name}")
        print(f"Lv : {self.level:5}")
        print(f"HP : {self.hitpoint:5}")
        print(f"MP : {self.magicpower:5}")
        print(f"ST : {self.strength:5}")
        print(f"DF : {self.defence:5}")
        print(f"WS : {self.wisdom:5}")
        print(f"EXP: {self.exp:5}")



class Fighter(Role):

    def __init__(self, level) -> None:
        super().__init__(level)
        self.name = "Fighter"
        self.init()
        self._id = 1


    def init(self) -> None:
        self.hitpoint = 32 * self.level
        self.magicpower = 4 * self.level
        self.strength = 12 * self.level
        self.defence = 10 * self.level
        self.wisdom = 8 * self.level




class Wizard(Role):

    def __init__(self, level) -> None:
        super().__init__(level)
        self.name = "Wizard"
        self.init()
        self._id = 2


    def init(self) -> None:
        self.hitpoint = 24 * self.level
        self.magicpower = 16 * self.level
        self.strength = 6 * self.level
        self.defence = 6 * self.level
        self.wisdom = 14 * self.level




class Sage(Role):

    def __init__(self, level) -> None:
        super().__init__(level)
        self.name = "Sage"
        self.init()
        self._id = 3


    def init(self) -> None:
        self.hitpoint = 27 * self.level
        self.magicpower = 14 * self.level
        self.strength = 8 * self.level
        self.defence = 8 * self.level
        self.wisdom = 18 * self.level




if __name__ == "__main__":
    fighter = Fighter(1)
    fighter.show()

    wizard = Wizard(100)
    wizard.show()

    sage = Sage(50)
    sage.show()