from games.cui.textbasedrpg.simpleRPG.interface.player import IPlayer


class Player(IPlayer):
    def __init__(self, name) -> None:
        super().__init__(name)