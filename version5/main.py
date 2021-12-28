import os
import sqlite3

from settings import DATABASE_DIR_PATH


def create_dirs():
    if not os.path.exists(DATABASE_DIR_PATH):
        print("NOT EXISTS")
        os.mkdir(DATABASE_DIR_PATH)
        print("CREATED")
    return os.path.exists(DATABASE_DIR_PATH)

# create_dirs()

con = sqlite3.connect(":memory:")
cur = con.cursor()

class PlayerMasterSql:
    def __init__(self, cur) -> None:
        self.table_name = "player_master"
        self.cur = cur

    def create(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")

    def insert(self, player_name):
        insert_sql = f"INSERT INTO player_master(name) VALUES ('{player_name}')"
        self.cur.execute(insert_sql)



pms = PlayerMasterSql(cur)
pms.create()
player_count = cur.execute("SELECT COUNT(*) FROM player_master").fetchone()[0]
if 0 == player_count:
    player_name = input("名前を入力してください > ")
    pms.insert(player_name)

print("どのプレイヤーでプレイしますか?")
for idx, name in cur.execute("SELECT * FROM player_master"):
    print(idx, name)
player_idx = int(input("> "))

cur.execute("CREATE TABLE IF NOT EXISTS player_status (id int, money int, class_id int, rank_exp int)")
cur.execute("INSERT INTO player_status VALUES (?, ?, ?, ?)", (1, 0, 0, 0))

cur.execute("UPDATE player_status SET rank_exp=1000 WHERE id={}".format(player_idx))
rank_data = [(i, 10*(i-1)) for i in range(1, 21)]

cur.execute("CREATE TABLE IF NOT EXISTS rank_master (rank_id int, rank_exp int)")
cur.executemany("INSERT INTO rank_master VALUES (?, ?)", rank_data)

player_rank = cur.execute("SELECT MAX(rank_id) FROM rank_master as rm JOIN player_status as ps WHERE ps.rank_exp >= rm.rank_exp AND ps.id={}".format(player_idx)).fetchone()[0]

cur.execute("CREATE TABLE IF NOT EXISTS class_master (class_id int, class_name text, rank_id int)")
class_data = [
    (0, "戦士", 0),
    (1, "僧侶", 0),
    (2, "魔法使い", 0),
    (3, "アサシン", 10),
    (4, "勇者", 15)
]
cur.executemany("INSERT INTO class_master VALUES (?, ?, ?)", class_data)

idx, name = cur.execute("SELECT * FROM player_master WHERE id={}".format(player_idx)).fetchone()
print(f"{idx=} {name=} {player_rank=}")

for idx, name in cur.execute("SELECT * FROM player_master"):
    print(idx, name)
player_idx = int(input("> "))

player_rank = cur.execute(
    "SELECT MAX(rank_id) FROM rank_master as rm JOIN player_status as ps WHERE ps.rank_exp >= rm.rank_exp AND ps.id={}".format(player_idx)
    ).fetchone()[0]

idx, name = cur.execute("SELECT * FROM player_master WHERE id={}".format(player_idx)).fetchone()
print(f"{idx=} {name=} {player_rank=}")