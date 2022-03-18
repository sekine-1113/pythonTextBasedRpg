from simpleRPG2 import (
    ABC,
    os,
    random,
    sys,
    abstractmethod,
    copy,
    deepcopy,
    integer,
)


import json, os

def test_loader():
    class Loader:
        def __init__(self, base_dir=""):
            self._base_dir = base_dir

        def loads(self, data):
            return json.loads(data)

        def load(self, path):
            file = os.path.join(
                self._base_dir,
                path)
            with open(file, "r") as f:
                return json.load(f)


    data = '{"players":[]}'
    loader = Loader("./simpleRPG2/")
    print(loader.loads(data))
    # print(loader.load("players.json"))


def test_player_manager():
    save = {
        "players":
            [
                {
                    "id": 0,
                    "name": "alice"
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

    class PlayerManager:
        def __init__(self, players):
            self.__players = players

        def get(self, _id):
            for player in self.__players:
                if player.get("id") == _id:
                    return player
            return

        def add(self, player):
            self.__players.append(player)

        def make(self, name, _id=None):
            if _id is not None:
                self.add({
                    "id": _id,
                    "name": name
                })
                return
            usable_id = []
            for i in range(self.size()+1):
                if self.get(i) is None:
                    usable_id.append(i)
            char_id = min(usable_id)
            self.add({
                "id": char_id,
                "name": name
            })


        def dumps(self):
            for player in self.__players:
                print(player)

        def size(self):
            return len(self.__players)

        def clear(self):
            self.__players = []

        def sort(self):
            pass



    players = save.get("players")
    player_manager = PlayerManager(players)
    player_manager.clear()
    if (0 == player_manager.size()):
        player_manager.make("peach")
    player = deepcopy(player_manager.get(0))
    print(player)
    player["id"] = 3
    player["name"] = "bes"
    player_manager.add(player)
    player_manager.make("jack")
    player_manager.make("bob", 5)
    print(player_manager.get(3))
    player_manager.dumps()


if __name__ == "__main__":
    test_loader()
    test_player_manager()