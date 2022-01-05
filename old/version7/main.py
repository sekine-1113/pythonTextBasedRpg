import sqlite3
import csv
from pathlib import Path
from sqlite3.dbapi2 import Connection, Cursor

from settings import (
    DATABASE_DIR_PATH, DATABASE_FILE_PATH, BackGroundColor, Color, Input, Singleton, exsits, mkdirs, unlock_ansi)

from battle_prototype import Battle
from enemy import EnemyFactory
from player import PlayerDataBase, PlayerFactory
from quest import QuestsDataBase


class RPG_CALL_ONCE(Singleton):
    def __init__(self, database: Path|str):
        # mkdirs(DATABASE_DIR_PATH)
        unlock_ansi()
        mkdirs(DATABASE_DIR_PATH)
        self.insert = not exsits(database)
        self.con: Connection = sqlite3.connect(database)
        self.cur: Cursor = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_status (id int, money int, class_id int, rank_exp int)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS player_classes_exp (id int, class_id int, class_exp int)")
        if self.insert:
            for i in range(1, 7):
                self.cur.execute("INSERT INTO player_classes_exp VALUES (0, ?, 0)", (i, ))
        self.cur.execute("CREATE TABLE IF NOT EXISTS rank_master (rank_id int, rank_exp int)")
        if self.insert:
            self.insert_rank_master()
        self.cur.execute("CREATE TABLE IF NOT EXISTS class_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, rank_id int)")
        if self.insert:
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
        if self.insert:
            self.insert_class_status_master()
        self.make_abilities_table()
        self.make_class_ability_table()
        # self.cur.execute("CREATE TABLE IF NOT EXISTS quests_master (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
        self.make_quests_table()
        self.make_enemies_table()
        self.con.commit()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def insert_class_master(self):
        with open(r"data\classes_master.csv", "r", encoding="UTF-8") as f:
            class_data = [row[1:] for row in csv.reader(f)]
        self.cur.executemany("INSERT INTO class_master(name, rank_id) VALUES (?, ?)", class_data)

    def insert_class_status_master(self):
        with open(r"data\classes_status_master.csv", "r", encoding="UTF-8") as f:
            data = [row for row in csv.reader(f)]
        self.cur.executemany("INSERT INTO class_status_master VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)

    def get_class_status(self):
        for row in self.cur.execute("SELECT * FROM class_status_master"):
            print(row)

    def insert_rank_master(self):
        rank_data = [(i, 10*(i-1)) for i in range(1, 21)]
        self.cur.executemany("INSERT INTO rank_master VALUES (?, ?)", rank_data)

    def make_class_ability_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS classes_ability_master (id int, level int, ability_id int)")
        if self.insert:
            with open(r"data\classes_abilities_master.csv", "r", encoding="UTF-8") as f:
                data = [row for row in csv.reader(f)]
            self.cur.executemany("INSERT INTO classes_ability_master VALUES (?, ?, ?)", data)

    def make_abilities_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS ability (id int, name text, description text, count int, fixed_value int, value int, target int, type int)")
        if self.insert:
            with open(r"data\abilities_master.csv", "r", encoding="utf-8") as f:
                abilities = [row for row in csv.reader(f)]
            self.cur.executemany("INSERT INTO ability VALUES (?, ?, ?, ?, ?, ?, ?, ?)", abilities)

    def make_enemies_table(self):
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
        if self.insert:
            with open(r"data\enemies_master.csv", "r", encoding="UTF-8") as f:
                enemies = [row for row in csv.reader(f)]
            self.cur.executemany("INSERT INTO enemies_master VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", enemies)

    def make_quests_table(self):
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
        if self.insert:
            with open(r"data\quests_master.csv", "r", encoding="UTF-8") as f:
                quests = [row[1:] for row in csv.reader(f)]
            self.cur.executemany("""INSERT INTO quests_master(name, description, enemy_id, difficulty, money, rank_exp)
                    VALUES (?, ?, ?, ?, ?, ?)""", quests)

    def get_cursor(self):
        return self.cur

    def get_connect(self):
        return self.con

    def close(self):
        self.con.commit()
        self.cur.close()
        self.con.close()



def main():
    with RPG_CALL_ONCE(DATABASE_FILE_PATH) as once:
        cur = once.get_cursor()  # データベースオブジェクトの取得
        player_factory = PlayerFactory(cur, PlayerDataBase)  # プレイヤーオブジェクトのファクトリークラス
        player = player_factory.create(1)  # プレイヤーオブジェクトを生成
        # player.show_status()
        # player.add_rank_sql(1000)  # ランクEXPに加算
        player.show_status()
        while True:

            player_entity = player.get_entity()
            # quest
            quests = QuestsDataBase(cur)
            quest_idx = quests.filtered_select()
            if quest_idx == -1:
                continue
            quest = quests.get_entity(quest_idx)
            #
            enemy_factory = EnemyFactory(cur)
            enemy = enemy_factory.create(quest.enemy_id)
            enemy_entity = enemy.get_entity()
            print("#5 OK")
            result = Battle(player_entity, enemy_entity).turn_clock()
            print("#6 OK")
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
    try:
        main()
    except Exception as e:
        print(e)
        input()