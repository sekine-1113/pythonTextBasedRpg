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

import json



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

    class PlayerManager:
        def __init__(self, players: list) -> None:
            self.__players = players

        def get(self, _id: int) -> dict|None:
            for player in self.__players:
                if player.get("id") == _id:
                    return player

        def add(self, player: dict) -> None:
            self.__players.append(player)

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
                self.add({
                    "id": _id,
                    "name": name
                })
                return

            char_id: int = min(usable_ids)
            self.add({
                "id": char_id,
                "name": name
            })

        def dumps(self) -> None:
            player: dict
            for player in self.__players:
                print(player)

        def size(self) -> int:
            return len(self.__players)

        def clear(self) -> None:
            self.__players = []

        def sort(self) -> None:
            self.__players.sort(key=lambda x: x["id"])

        def output(self) -> dict:
            return {"players": self.__players}


    player_manager = PlayerManager(save.get("players"))
    print(f"{player_manager.output()=}")
    player_manager.clear()
    if (0 == player_manager.size()):
        player_manager.make("peach")
    player_manager.add({"id": 5, "name":"mike"})
    player_manager.make("jack")
    player_manager.make("bob")
    player_manager.make("wendy", 1)
    print(f"{player_manager.get(3)=}")
    player_manager.sort()
    player_manager.dumps()

    print(f"{player_manager.output()=}")


    class FileManager:
        def __init__(self, base_dir=""):
            self._base_dir = base_dir

        def load(self, path: str) -> dict:
            file = os.path.join(
                self._base_dir,
                path)
            with open(file, "r", encoding="UTF-8") as f:
                return json.load(f)

        def save(self, path: str, data: object) -> None:
            file: str = os.path.join(self._base_dir, path)
            with open(file, "w", encoding="UTF-8") as f:
                json.dump(data, f, indent=4)


    # fm = FileManager("./simpleRPG2")
    # fm.save("data/players.json", player_manager.output())


if __name__ == "__main__":
    test_player_manager()