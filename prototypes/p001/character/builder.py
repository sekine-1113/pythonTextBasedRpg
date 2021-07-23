from games.cui.textbasedrpg.prototypes.p001.character.player import Player


class Builder:
    def build(self):
        pass


class PlayerBuilder(Builder):
    def __init__(self) -> None:
        self._name = None

    def name(self, nn):
        self._name = nn

    def build(self):
        return Player(self._name, 0, 0, 0, 0)




player_builder = PlayerBuilder()
player_builder.name("アリス")
player = player_builder.build()
print(player.name)