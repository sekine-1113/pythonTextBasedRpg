
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

    def execute_command(self, command_name):
        cmd = self.commands.get(
            command_name,
            AttackCommand())
        self.commands_history.append(cmd)
        return cmd.execute()

    def execute_commands(self, commands_name):
        return [self.execute_command(cmd_name) for cmd_name in commands_name]


    def replay(self, n, reverse=False):
        history = self.commands_history[-n:]
        if reverse:
            history = reversed(history)
        for cmd in history:
            cmd.execute()

player = Player()
player.execute_commands(["attack", "heal"])
player.execute_command("attack")
player.replay(2)