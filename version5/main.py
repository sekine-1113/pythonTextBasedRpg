import os
import sqlite3
from sqlite3.dbapi2 import Cursor

from settings import DATABASE_DIR_PATH
from player import PlayerFactory


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

    def count_regist(self) -> bool:
        return self.cur.execute("SELECT COUNT(*) FROM player_master").fetchone()[0]

    def start(self):
        if self.count == 0:
            self.regist()
        return self.select()

class Player:
    def __init__(self, cur, idx=1) -> None:
        self.cur = cur
        self.idx = idx

    def get_status(self):
        money, class_id, rank_exp = self.cur.execute("SELECT money, class_id, rank_exp FROM player_status WHERE id={}".format(self.idx)).fetchall()[0]
        return money, class_id, rank_exp


once = RPG_CALL_ONCE(":memory:")

cur = once.get_cursor()
player_db = PlayerDataBase(cur)

player_idx, player_name = player_db.start()
player = Player(cur)
player.get_status()

player_rank = player.status.get_rank_sql(cur)

idx, name = player.get_player(cur)
print(f"{idx=} {name=} {player_rank=}")

player.status.add_rank_exp(1000)
player.status.set_rank_sql(cur)
idx, name = player.get_player(cur)
player_rank = player.status.get_rank_sql(cur)
print(f"{idx=} {name=} {player_rank=}")