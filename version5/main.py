import os
import sqlite3

from settings import DATABASE_DIR_PATH


def mkdirs(dirs_path) -> bool:
    if not os.path.exists(dirs_path):
        os.makedirs(dirs_path)
    return os.path.exists(dirs_path)

# mkdirs(DATABASE_DIR_PATH)


class RPG_CALL_ONCE:
    def __init__(self, database):
        self.con = sqlite3.connect(database)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_status (id int, money int, class_id int, rank_exp int)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS rank_master (rank_id int, rank_exp int)")
        self.insert_rank_master()
        self.cur.execute("CREATE TABLE IF NOT EXISTS class_master (class_id INTEGER PRIMARY KEY AUTOINCREMENT, class_name text, rank_id int)")
        self.insert_class_master()
        self.con.commit()


    def insert_class_master(self):
        class_data =  [
            ("戦士", 0),
            ("僧侶", 0),
            ("魔法使い", 0),
            ("アサシン", 10),
            ("勇者", 15)
        ]
        self.cur.executemany("INSERT INTO class_master(class_name, rank_id) VALUES (?, ?)", class_data)

    def insert_rank_master(self):
        rank_data = [(i, 10*(i-1)) for i in range(1, 21)]
        self.cur.executemany("INSERT INTO rank_master VALUES (?, ?)", rank_data)

    def get_cursor(self):
        return self.cur


class PlayerDataBase:
    def __init__(self, cur) -> None:
        self.cur = cur
        self.count = self.count_regist()

    def select(self, _format="{} {}"):
        print("どのプレイヤーでプレイしますか?")
        for idx, name in self.cur.execute("SELECT * FROM player_master"):
            print(_format.format(idx, name))
        idx = int(input("> "))
        return self.cur.execute("SELECT id, name FROM player_master WHERE id={}".format(idx)).fetchone()

    def regist(self):
        name = input("名前を入力してください: ")
        self.cur.execute("INSERT INTO player_master(name) VALUES ('{}')".format(name))
        self.count = self.count_regist()
        self.cur.execute("INSERT INTO player_status VALUES (?, ?, ?, ?)", (self.count, 0, 1, 0))

    def is_regist(self, idx):
        return self.cur.execute("SELECT COUNT(*) FROM player_master WHERE id={}".format(idx)).fetchone()[0] == 1

    def count_regist(self) -> bool:
        return self.cur.execute("SELECT COUNT(*) FROM player_master").fetchone()[0]

    def start(self):
        if self.count == 0:
            self.regist()
        return self.select()



class Player:
    def __init__(self, cur, idx) -> None:
        self.cur = cur
        self.idx = idx

    def get_player(self):
        idx, name = self.cur.execute("SELECT id, name FROM player_master WHERE id={}".format(self.idx)).fetchone()
        return idx, name

    def get_status(self):
        money, class_id, rank_exp = self.cur.execute("SELECT money, class_id, rank_exp FROM player_status WHERE id={}".format(self.idx)).fetchall()[0]
        return money, class_id, rank_exp

    def get_rank_exp(self):
        rank_exp = self.cur.execute("SELECT rank_exp FROM player_status WHERE id={}".format(self.idx)).fetchone()[0]
        return rank_exp

    def get_rank_sql(self):
        return self.cur.execute(
            """
            SELECT MAX(rank_id) FROM rank_master JOIN player_status
            WHERE (player_status.rank_exp >= rank_master.rank_exp)
            AND player_status.id={}""".format(self.idx)).fetchone()[0]

    def set_rank_sql(self, exp=0):
        rank_exp = int(self.get_rank_exp()) + exp
        self.cur.execute("UPDATE player_status SET rank_exp={} WHERE id={}".format(rank_exp, self.idx))


class PlayerFactory:
    def __init__(self, cur, player_database: PlayerDataBase) -> None:
        self.cur = cur
        self.player_database = player_database(self.cur)

    def create(self, idx):
        if self.check(idx):
            return Player(cur, idx)
        self.player_database.regist()
        return Player(cur, idx)

    def check(self, idx):
        return self.player_database.is_regist(idx)


def show_player(player):
    idx, name = player.get_player()
    player_rank = player.get_rank_sql()
    print(f"{idx=} {name=} {player_rank=}")


once = RPG_CALL_ONCE(":memory:")  # 初期化及びデータベースの構築
cur = once.get_cursor()  # データベースオブジェクトの取得
player_factory = PlayerFactory(cur, PlayerDataBase)  # プレイヤーオブジェクトのファクトリークラス
player = player_factory.create(1)  # プレイヤーオブジェクトを生成
player2 = player_factory.create(2)  # プレイヤーオブジェクトを生成
show_player(player)
player.set_rank_sql(1000)  # ランクEXPに加算
show_player(player)
show_player(player2)