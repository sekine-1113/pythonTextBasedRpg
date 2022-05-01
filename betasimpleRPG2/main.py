from betasimpleRPG2.tests import (
    jsonconverter
)



def test_player_manager():

    save = {
        "players": [
            {
                "id": 0,
                "name": "alice",
            },
            {
                "id": 1,
                "name": "bob"
            },
            {
                "id": 2,
                "name": "stefan"
            }
        ]
    }

    class Player:
        def __init__(self, player_id, name) -> None:
            self.id = player_id
            self.name = name

        def __repr__(self) -> str:
            return f"{self.id} {self.name}"

    class PlayerManager:
        def __init__(self, players: list[Player]) -> None:
            self.players = players

        def get(self, _id: int) -> dict|None:
            player: Player
            for player in self.players:
                if player.id == _id:
                    return player

        def add(self, player: Player) -> None:
            self.players.append(player)

        def get_usable_ids(self) -> list[int]:
            i: int
            usable_ids: list[int] = []
            for i in range(self.size()+1):
                if self.get(i) is None:
                    usable_ids.append(i)
            return usable_ids

        def make(self, name: str, _id: int=None) -> None:
            usable_ids: list[int] = self.get_usable_ids()
            if _id is not None and _id in usable_ids:
                self.add(Player(_id, name))
                return

            char_id: int = min(usable_ids)
            self.add(Player(char_id, name))

        def dumps(self) -> None:
            player: Player
            for player in self.players:
                print(player)

        def size(self) -> int:
            return len(self.players)

        def clear(self) -> None:
            self.players = []

        def sort(self) -> None:
            self.players.sort(key=lambda x: x.id)

        def tojson(self) -> dict:
            return jsonconverter.tojson(self)



    players = []
    for player in save.get("players"):
        players.append(Player(player_id=player.get("id"), name=player.get("name")))
    player_manager = PlayerManager(players)
    print(f"{player_manager.tojson()=}")
    player_manager.clear()
    if (0 == player_manager.size()):
        player_manager.make("peach")
    player_manager.add(Player(5, "alice"))
    player_manager.make("jack")
    player_manager.make("bob")
    player_manager.make("wendy", 1)
    print(f"{player_manager.get(3)=}")
    player_manager.sort()

    save["players"] = jsonconverter.tojson(player_manager)
    print(save["players"])



    # fm = FileManager("./simpleRPG2")
    # fm.save("data/players.json", player_manager.output())


if __name__ == "__main__":
    test_player_manager()
    # OK,,,