from games.cui.textbasedrpg.simpleRPG.interface.player import IPlayer


info = {
    "name": "Alice",
    "player_id": "b8fy8jop",
    "status": {
        "aaa": {
            "hit_point": 100,
            "strength": 33
            },
        "bbb": {
            "hit_point": 100,
            "strength": 24
        }
    }
}


class Player(IPlayer):
    def __init__(self, name) -> None:
        super().__init__(name)


class MockPlayer(IPlayer):
    def __init__(self, name="test") -> None:
        super().__init__(name)


if __name__ == "__main__":
    player = Player(info["name"])