
def yes_or_no(prompt=""):
    check = input(prompt)
    return check.lower() in ("y", "yes")


class Game:
    def __init__(self) -> None:
        self.loop:bool = True
        self.debug:bool = False

    def mainloop(self):
        print("Welcome to QuestRPG!")
        while self.loop:
            print("1: Start")
            print("2: Config")
            print("0: Exit")
            user_input = input("> ")
            if user_input.isdigit():
                user_input = int(user_input)
                match user_input:
                    case 1:
                        self.start()
                    case 2:
                        self.config()
                    case 0:
                        self.loop = False
                        print("See you!")
                    case _:
                        break

    def start(self):
        loop = True
        while loop:
            print("1: Quest")
            print("2: Equip")
            print("3: Status")
            print("0: Exit")
            user_input = input("> ")
            if user_input.isdigit():
                user_input = int(user_input)
                match user_input:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 0:
                        loop = False
                    case _:
                        break

    def config(self):
        print("debug mode:", self.debug)
        if yes_or_no("change debug mode?(y/n):"):
            self.debug = not self.debug





if __name__ == "__main__":
    game = Game()
    game.mainloop()

