import sys
import sqlite3
import random
from sqlite3.dbapi2 import Connection, Cursor
from pathlib import Path


from settings import Singleton, mkdirs, DATABASE_DIR_PATH
from utils.windows import Color, BackGroundColor, unlock_ansi
from battle_prototype import Battle


class Input(Singleton):
    @classmethod
    def integer(self, prompt="> "):
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            return self.integer(prompt)

    @classmethod
    def integer_with_range(self, prompt="> ", _min=0, _max=0):
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if _min <= user_input <= _max:
                return user_input
            return self.integer_with_range(prompt, _min, _max)
        except ValueError:
            return self.integer_with_range(prompt, _min, _max)


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


class AbilityEntity:
    def __init__(self, name, description, count, target, type_, fixed_value, value) -> None:
        self.name = name
        self.description = description
        self.count = count
        self.target = target
        self.type_ = type_
        self.fixed_value = fixed_value
        self.value = value

    def can_use(self):
        return self.count > 0

    def __repr__(self) -> str:
        return f"{self.name} {self.count}"


class ActorEntity:
    def __init__(self, hitpoint, strength, defence, magicpower, critical) -> None:
        self.hitpoint = hitpoint
        self.max_hitpoint = self.hitpoint
        self.strength = strength
        self.origin_strength = self.strength
        self.defence = defence
        self.origin_defence = self.defence
        self.magicpower = magicpower
        self.origin_magicpower = self.magicpower
        self.critical = critical
        self.abilities: list[AbilityEntity] = None

    def set_abilities(self, abilities) -> None:
        self.abilities = abilities

    def ability_select(self):
        for i, ability in enumerate(self.abilities, 1):
            print(i, ability.name)
        print(0, "リタイア")
        return Input.integer_with_range(_max=len(self.abilities))-1

    def get_ability(self, idx):
        return self.abilities[idx]

    def execute(self, idx) -> int:
        ability = self.get_ability(idx)
        if not ability.can_use():
            raise Exception
        ability.count -= 1
        critical = self.critical >= random.randint(0, 100) >= 0
        if critical:
            print("Critical!")
        if ability.type_ == 0:  # 攻撃
            damage = ability.fixed_value + ability.value * self.strength
            damage += damage * 0.2 * critical
            return damage
        elif ability.type_ == 1:  # 回復
            heal = ability.fixed_value + ability.value * self.magicpower
            heal += heal * 0.2 * critical
            return heal
        return 0

    def take_damage(self, damage):
        self.hitpoint -= (damage - self.defence)

    def take_heal(self, heal):
        if self.hitpoint + heal > self.max_hitpoint:
            heal = self.max_hitpoint - self.hitpoint
        self.hitpoint += heal

    def is_dead(self) -> bool:
        return self.hitpoint <= 0


class PlayerDataBase:
    def __init__(self, cur) -> None:
        self.cur: Cursor = cur
        self.count = self.count_regist()

    def select(self, _format="{} {}"):
        print("どのプレイヤーでプレイしますか?")
        for idx, name in self.cur.execute("SELECT * FROM player_master"):
            print(_format.format(idx, name))
        print("0 やめる")
        idx = Input.integer_with_range(_max=self.count)
        return self.cur.execute("SELECT id, name FROM player_master WHERE id=?", (idx,)).fetchone()

    def regist(self):
        name = input("名前を入力してください: ")
        self.cur.execute("INSERT INTO player_master(name) VALUES (?)", (name,))
        self.count = self.count_regist()
        self.cur.execute("INSERT INTO player_status VALUES (?, ?, ?, ?)", (self.count, 0, 1, 0))
        self.cur.execute("INSERT INTO player_classes_exp VALUES (?, ?, ?)", (self.count, 1, 0))
        self.cur.execute("INSERT INTO player_classes_exp VALUES (?, ?, ?)", (self.count, 2, 0))
        self.cur.execute("INSERT INTO player_classes_exp VALUES (?, ?, ?)", (self.count, 3, 0))
        self.cur.execute("INSERT INTO player_classes_exp VALUES (?, ?, ?)", (self.count, 4, 0))
        self.cur.execute("INSERT INTO player_classes_exp VALUES (?, ?, ?)", (self.count, 5, 0))
        self.cur.execute("INSERT INTO player_classes_exp VALUES (?, ?, ?)", (self.count, 6, 0))

    def is_regist(self, idx):
        return self.cur.execute("SELECT COUNT(*) FROM player_master WHERE id=?", (idx,)).fetchone()[0] == 1

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

    def get_class_status(self):
        class_id = self.get_class_id()
        level = self.get_level()
        return self.cur.execute("""
            SELECT hitpoint, strength, defence, magicpower, critical
            FROM class_status_master
            WHERE id=?
            AND level=?
            """, (class_id, level)
        ).fetchall()[0]

    def get_entity(self):
        entity = ActorEntity(*self.get_class_status())
        entity.set_abilities(self.get_abilities())
        return entity

    def get_player(self):
        idx, name = self.cur.execute("SELECT id, name FROM player_master WHERE id=?", (self.idx,)).fetchone()
        return idx, name

    def set_class_id(self, class_id):
        self.cur.execute("UPDATE player_status SET class_id=? WHERE id=?", (class_id, self.idx))

    def get_class_id(self):
        return self.cur.execute("SELECT class_id FROM player_status").fetchone()[0]

    def get_class(self):
        class_id = self.get_class_id()
        cls_name = self.cur.execute(
            "SELECT name FROM class_master WHERE id=?", (class_id,)
        ).fetchone()[0]
        return cls_name

    def get_status(self):
        money, class_id, rank_exp = self.cur.execute(
            "SELECT money, class_id, rank_exp FROM player_status WHERE id=?", (self.idx, )).fetchall()[0]
        return money, class_id, rank_exp

    def set_money(self, money):
        self.cur.execute("UPDATE player_status SET money=? WHERE id=?", (money, self.idx))

    def get_abilities(self):
        level = self.get_level()
        abilities = self.cur.execute(
            """
            SELECT ability.name, ability.description, ability.count, ability.target, ability.type, ability.fixed_value, ability.value
            FROM ability
            JOIN classes_ability_master
            WHERE ability.id=classes_ability_master.ability_id
            AND classes_ability_master.level<=?
            """, (level,)
        ).fetchall()
        for i, ability in enumerate(abilities):
            abilities[i] = AbilityEntity(*ability)
        return abilities

    def get_rank_exp(self):
        rank_exp = self.cur.execute("SELECT rank_exp FROM player_status WHERE id=?", (self.idx,)).fetchone()[0]
        return rank_exp

    def get_rank(self):
        return self.cur.execute(
            """
            SELECT MAX(rank_id) FROM rank_master JOIN player_status
            WHERE (player_status.rank_exp >= rank_master.rank_exp)
            AND player_status.id=?""", (self.idx,)).fetchone()[0]

    def get_class_exp(self):
        class_id = self.get_class_id()
        return self.cur.execute("SELECT * FROM player_classes_exp WHERE player_classes_exp.class_id=?", (class_id, )).fetchone()[0]

    def add_class_exp(self, exp=0):
        class_exp = int(self.get_class_exp()) + exp
        self.cur.execute("UPDATE player_classes_exp SET class_exp=? WHERE id=?", (class_exp, self.idx))

    def get_level(self):
        return self.cur.execute(
            """
            SELECT MAX(csm.level) FROM (SELECT id, class_id FROM player_status) as ps
            JOIN  player_classes_exp
            JOIN (SELECT id, level, need_exp FROM class_status_master) as csm
            WHERE ps.class_id=player_classes_exp.class_id
            AND player_classes_exp.class_id=csm.id
            AND ps.id=?
            AND player_classes_exp.id=?
            AND player_classes_exp.class_exp >= csm.need_exp
            """, (self.idx, self.idx)).fetchone()[0]

    def add_rank_sql(self, exp=0):
        rank_exp = int(self.get_rank_exp()) + exp
        self.cur.execute("UPDATE player_status SET rank_exp=? WHERE id=?", (rank_exp, self.idx))

    def rename(self):
        name = input("新しい名前を入力してください: ")
        self.cur.execute("UPDATE player_master SET name=? WHERE id=?", (name, self.idx))

    def show_status(self):
        class_status = self.get_class_status()
        print("名前:", self.get_player()[1])
        print("ランク:", self.get_rank())
        print("ゴールド:", self.get_status()[0])
        print("クラス:", self.get_class())
        print("レベル:", self.get_level())
        print("ステータス")
        print("HP:", class_status[0])
        print("攻撃力:", class_status[1])
        print("守備力:", class_status[2])
        print("魔力:", class_status[3])
        print("会心率:", class_status[4])


class PlayerFactory:
    def __init__(self, cur, player_database: PlayerDataBase) -> None:
        self.cur: Cursor = cur
        self.player_database: PlayerDataBase = player_database(self.cur)

    def create(self, idx):
        if self.check(idx):
            return Player(self.cur, idx)
        self.player_database.regist()
        idx = self.player_database.count_regist()
        return Player(self.cur, idx)

    def check(self, idx):
        return self.player_database.is_regist(idx)


class EnemyFactory:
    def __init__(self) -> None:
        pass


def main():
    with RPG_CALL_ONCE(":memory:") as once:
        cur = once.get_cursor()  # データベースオブジェクトの取得
        player_factory = PlayerFactory(cur, PlayerDataBase)  # プレイヤーオブジェクトのファクトリークラス
        player = player_factory.create(1)  # プレイヤーオブジェクトを生成
        player.show_status()
        # player.add_rank_sql(1000)  # ランクEXPに加算
        # aplayer.set_class_id(2)
        # player.add_class_exp(1000)
        player.show_status()
        player_entity = player.get_entity()
        result = Battle(player_entity, player_entity).turn_clock()
        if result == 0:
            print("you lose")
        elif result == 1:
            old_level = player.get_level()
            old_rank = player.get_rank()
            player.add_class_exp(1000)
            player.add_rank_sql(1000)
            player.set_money(player.get_status()[0]+1000)
            new_level = player.get_level()
            new_rank = player.get_rank()
            diff_level = new_level - old_level
            diff_rank = new_rank - old_rank
            if diff_level > 0:
                print("Level Up!")
            if diff_rank > 0:
                print("Rank Up!")
            print("you win")
        elif result == -1:
            print("撤退した")
        player.show_status()


if __name__ == "__main__":
    main()