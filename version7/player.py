from settings import Input

from ability import AbilityEntity
from actor import ActorEntity


class PlayerDataBase:
    def __init__(self, cur) -> None:
        self.cur = cur
        self.count = self.count_regist()

    def select(self, _format="{} {}") -> tuple:
        print("どのプレイヤーでプレイしますか?")
        for idx, name in self.cur.execute("SELECT * FROM player_master"):
            print(_format.format(idx, name))
        print("0 やめる")
        idx = Input.integer_with_range(_max=self.count)
        return self.cur.execute("SELECT id, name FROM player_master WHERE id=?", (idx,)).fetchone()

    def regist(self) -> None:
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

    def is_regist(self, idx: int) -> bool:
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

    def get_class_status(self) -> tuple:
        class_id = self.get_class_id()
        level = self.get_level()
        return self.cur.execute("""
            SELECT hitpoint, strength, defence, magicpower, critical
            FROM class_status_master
            WHERE id=?
            AND level=?
            """, (class_id, level)
        ).fetchall()[0]

    def get_entity(self) -> ActorEntity:
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
        self.cur = cur
        self.player_database: PlayerDataBase = player_database(self.cur)

    def create(self, idx):
        if self.check(idx):
            return Player(self.cur, idx)
        self.player_database.regist()
        idx = self.player_database.count_regist()
        return Player(self.cur, idx)

    def check(self, idx):
        return self.player_database.is_regist(idx)
