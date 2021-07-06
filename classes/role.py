
class Role:

    def __init__(self, id: int, name: str, available: int, command: list, stats: dict) -> None:
        self.id = id
        self.name = name
        self.available = available
        self.command = command
        self.stats = stats


    def choose_command(self):
        for i, cmd in enumerate(self.command, 1):
            print(i, cmd)
        print(0, "Escape")
        choice = input("> ")
        return int(choice)

    def attack(self, target=None):
        print(self.name, "'s attaked!", sep="")


role = Role(0, "Fighter", 1, ["Attack"], {""})

if role.choose_command() == 1:
    role.attack()


