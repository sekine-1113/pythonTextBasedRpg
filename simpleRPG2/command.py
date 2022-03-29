
class Command:
    def execute(self, *args, **kwargs):
        return


class AttackCommand(Command):
    def execute(self, *args, **kwargs):
        print("attack")
        return "attack"


class HealCommand(Command):
    def execute(self, *args, **kwargs):
        print("healing")
        return "healing"


class Player:
    def __init__(self):
        self.commands = {
            "attack": AttackCommand(),
            "heal": HealCommand()
        }
        self.commands_history = []

    def command_execute(self, command_name):
        cmd = self.commands.get(
            command_name,
            AttackCommand())
        self.commands_history.append(cmd)
        return cmd.execute()

    def replay(self, n, reverse=False):
        history = self.commands_history[-n:]
        if reverse:
            history = reversed(history)
        for cmd in history:
            cmd.execute()

player = Player()
player.command_execute("attack")
player.command_execute("heal")
player.command_execute("attack")
player.replay(2)
