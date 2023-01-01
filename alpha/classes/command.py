from games.cui.textbasedrpg.alpha.interface._command import _Command


class Command(_Command):

    def __init__(self, cmd) -> None:
        self.cmd = cmd

    def execute(self):
        self.cmd()
        return True


class RunCommand(_Command):

    def execute(self):
        return False