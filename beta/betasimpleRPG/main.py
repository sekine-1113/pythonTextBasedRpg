from betasimpleRPG import Singleton
from betasimpleRPG.concrete import (
    Enemy,
    EnemyStatus,
    Player,
    PlayerStatus,
)
from betasimpleRPG.io import (
    integer,
)
from betasimpleRPG.io.file import (
    load,
    dump,
    exists,
)


class DataLoader(Singleton):

    def __init__(self) -> None:
        self.__data: dict[str, dict] = {}

    def create(self, path: str, data: dict) -> None:
        print(path, data)
        # dump(path, data)

    def regist(self, key: str, path: str) -> dict:
        if exists(path):
            self.__data[key] = load(path)
            return self.get(key)
        raise Exception

    def get(self, key: str) -> dict:
        return self.__data.get(key)


class PlayerFactory:

    def __init__(self, data: dict) -> None:
        self._data = data

    def create(self, index: int):
        player_data = self._data[index]
        return Player(
            name=player_data.get("name"),
            status=PlayerStatus(
                level=player_data.get("status").get("level"),
                HP=player_data.get("status").get("HP"),
                ATK=player_data.get("status").get("ATK"),
                DEF=player_data.get("status").get("DEF"),
                EXP=player_data.get("status").get("EXP"),
            ),
            money=player_data.get("money"),
        )

    def choose(self):
        for i, player in enumerate(self._data):
            print(i, player["name"])
        return integer()


class EnemyFactory:

    def __init__(self, data) -> None:
        self._data = data

    def create(self, index: int) -> Enemy:
        enemy_data = self._data[index]
        return Enemy(
            name=enemy_data.get("name"),
            status=EnemyStatus(
                level=enemy_data.get("status").get("level"),
                HP=enemy_data.get("status").get("HP"),
                ATK=enemy_data.get("status").get("ATK"),
                DEF=enemy_data.get("status").get("DEF"),
                EXP=enemy_data.get("status").get("EXP"),
            ),
            money=enemy_data.get("money"),
        )



def main():

    loader = DataLoader()

    master_data = loader.regist("master", r"simpleRPG\data\master.json")
    player_data = loader.regist("player", r"simpleRPG\data\player.json")

    player_factory = PlayerFactory(
        data=player_data.get("players"),
    )
    player_index = player_factory.choose()
    player = player_factory.create(index=player_index)

    enemy_factory = EnemyFactory(data=master_data.get("enemies"))
    enemy = enemy_factory.create(index=0)

    print(player)
    print(enemy)


if __name__ == "__main__":
    print((
        f"(ゲームタイトル)\n"
        f"1: つづきから\n"
        f"2: とうろく\n"
        f"0: おわる\n"
    ))

    print((
        f"(つづきから)\n"
        f"キャラ数0  -> とうろく\n"
        f"キャラ数1~ -> マイページ\n"
    ))

    print((
        f"(とうろく)\n"
        f"プレイヤーを登録してファイルに書き込む\n"
    ))

    print((
        f"(マイページ)\n"
        f"1: クエスト\n"
        f"2: つよさ\n"
        f"0: おわる\n"
    ))

    print((
        f"(クエスト)\n"
        f"1: 敵\n"
        f"0: おわる\n"
    ))

    print((
        f"(つよさ)\n"
        f"つよさを出力\n"
        f"(そうび)\n"
    ))