import sqlite3
from pathlib import Path
from sqlite3.dbapi2 import Connection, Cursor

from settings import (
    DATABASE_DIR_PATH, BackGroundColor, Color, Input, Singleton, mkdirs, unlock_ansi)

from battle_prototype import Battle
from enemy import EnemyFactory
from player import PlayerDataBase, PlayerFactory
from quest import QuestsDataBase


class RPG_CALL_ONCE(Singleton):
    def __init__(self, database: Path|str):
        # mkdirs(DATABASE_DIR_PATH)
        unlock_ansi()
        self.con: Connection = sqlite3.connect(database)
        self.cur: Cursor = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_status (id int, money int, class_id int, rank_exp int)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_classes_exp (id int, class_id int, class_exp int)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS rank_master (rank_id int, rank_exp int)")
        self.insert_rank_master()
        self.cur.execute("CREATE TABLE IF NOT EXISTS class_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, rank_id int)")
        self.insert_class_master()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS class_status_master (
            id int,
            level int,
            hitpoint int,
            strength int,
            defence int,
            magicpower int,
            critical int,
            need_exp)""")
        self.insert_class_status_master()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ability (id int, name text, description text, count int, target int, type int, fixed_value int, value int)")
        self.cur.execute("INSERT INTO ability VALUES (1, '2倍攻撃', '2倍の力で攻撃する', 15, 1, 0, 1, 2)")
        self.cur.execute("INSERT INTO ability VALUES (2, '3倍攻撃', '3倍の力で攻撃する', 10, 1, 0, 1, 3)")
        self.cur.execute("INSERT INTO ability VALUES (3, '回復', '回復する', 10, 0, 1, 10, 1)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS classes_ability_master (id int, level int, ability_id int)")
        self.cur.execute("INSERT INTO classes_ability_master VALUES (1, 1, 1)")
        self.cur.execute("INSERT INTO classes_ability_master VALUES (1, 2, 2)")
        self.cur.execute("INSERT INTO classes_ability_master VALUES (1, 3, 3)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS quests_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS quests_master (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                description text,
                enemy_id int,
                difficulty int,
                money int,
                rank_exp int
            )""")
        self.cur.execute("""INSERT INTO quests_master(name, description, enemy_id, difficulty, money, rank_exp)
                VALUES ('ゴブリン討伐', 'ゴブリンを討伐せよ', 1, 1, 10, 10)""")
        self.cur.execute("""INSERT INTO quests_master(name, description, enemy_id, difficulty, money, rank_exp)
                VALUES ('ドラゴン討伐', 'ドラゴンを討伐せよ', 2, 2, 20, 20)""")

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS enemies_master (
                    id int,
                    name text,
                    hitpoint int,
                    strength int,
                    defence int,
                    magicpower int,
                    critical int,
                    exp int,
                    ability_id int
                )
                """)
        self.cur.execute("""
                INSERT INTO enemies_master
                VALUES (1, 'ゴブリン', 24, 8, 4, 0, 0, 10, 1)
                """)
        self.cur.execute("""
                INSERT INTO enemies_master
                VALUES (2, 'ドラゴン', 54, 16, 12, 4, 0, 100, 1)
                """)
        self.cur.execute("""
                INSERT INTO enemies_master
                VALUES (2, 'ドラゴン', 54, 16, 12, 4, 0, 100, 2)
                """)
        self.con.commit()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def insert_class_master(self):
        class_data =  [
            ("戦士", 0),
            ("僧侶", 0),
            ("魔法使い", 0),
            ("アサシン", 10),
            ("勇者", 15)
        ]
        self.cur.executemany("INSERT INTO class_master(name, rank_id) VALUES (?, ?)", class_data)

    def insert_class_status_master(self):
        data = """1	  1   32	12	10	2	2	 0
                1   2	36	15	12	2	2	12
                1 	3	40	18	14	2	2	24
                1	4	44	21	16	2	2	36
                1	5	48	24	18	2	2	48
                1	6	52	27	20	2	2	60
                1	7	56	30	22	2	2	72
                1	8	60	33	24	2	2	84
                1	9	64	36	26	2	2	96
                1	10	68	39	28	2	2	108
                1	11	72	42	30	2	2	120
                1	12	76	45	32	2	2	132
                1	13	80	48	34	2	2	144
                1	14	84	51	36	2	2	156
                1	15	88	54	38	2	2	168
                1	16	92	57	40	2	2	180
                1	17	96	60	42	2	2	192
                1	18	100	63	44	2	2	204
                1	19	104	66	46	2	2	216
                1	20	108	69	48	2	2	228""".replace("\t", " ")
        data = list(map(lambda x: x.split(), data.split("\n")))
        for i, dt in enumerate(data):
            data[i] = tuple(map(int, dt))
        self.cur.executemany("INSERT INTO class_status_master VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)

    def get_class_status(self):
        for row in self.cur.execute("SELECT * FROM class_status_master"):
            print(row)

    def insert_rank_master(self):
        rank_data = [(i, 10*(i-1)) for i in range(1, 21)]
        self.cur.executemany("INSERT INTO rank_master VALUES (?, ?)", rank_data)

    def get_cursor(self):
        return self.cur

    def get_connect(self):
        return self.con

    def close(self):
        self.con.commit()
        self.cur.close()
        self.con.close()



def main():
    with RPG_CALL_ONCE(":memory:") as once:
        cur = once.get_cursor()  # データベースオブジェクトの取得
        player_factory = PlayerFactory(cur, PlayerDataBase)  # プレイヤーオブジェクトのファクトリークラス
        player = player_factory.create(1)  # プレイヤーオブジェクトを生成
        # player.show_status()
        # player.add_rank_sql(1000)  # ランクEXPに加算
        # aplayer.set_class_id(2)
        # player.show_status()
        player_entity = player.get_entity()
        # quest
        quests = QuestsDataBase(cur)
        quest_idx = quests.select()
        quest = quests.get_entity(quest_idx)
        #
        enemy_factory = EnemyFactory(cur)
        enemy = enemy_factory.create(quest.enemy_id)
        enemy_entity = enemy.get_entity()
        result = Battle(player_entity, enemy_entity).turn_clock()
        if result == 0:
            print("you lose")
        elif result == 1:
            print("you win")
            old_level = player.get_level()
            old_rank = player.get_rank()
            player.add_class_exp(enemy.get_exp())
            player.add_rank_sql(quest.rank_exp)
            player.set_money(player.get_status()[0]+quest.money)
            new_level = player.get_level()
            new_rank = player.get_rank()
            diff_level = new_level - old_level
            diff_rank = new_rank - old_rank
            if diff_level > 0:
                print("Level Up!")
            if diff_rank > 0:
                print("Rank Up!")
        elif result == -1:
            print("撤退した")
        player.show_status()


if __name__ == "__main__":
    main()
