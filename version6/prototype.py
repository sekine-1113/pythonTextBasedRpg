import sqlite3



class QuestEntity:
    def __init__(self, name, desc, enemy_id, deff, money, rank_exp) -> None:
        self.name = name
        self.desc = desc
        self.enemy_id = enemy_id
        self.deff = deff
        self.money = money
        self.rank_exp = rank_exp

    def __repr__(self) -> str:
        return self.name


class QuestsDataBase:
    def __init__(self, cur) -> None:
        self.cur = cur

    def select(self):
        quests = self.cur.execute("SELECT id, name FROM quests_master").fetchall()
        for quest in quests:
            print(*quest)
        return int(input("> "))

    def get_entity(self, idx):
        quest = self.cur.execute("SELECT name, description, enemy_id, defficulty, money, rank_exp FROM quests_master WHERE id=?", (idx, )).fetchone()
        return QuestEntity(*quest)

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
        self.abilities = None

    def set_abilities(self, abilities) -> None:
        self.abilities = abilities

class EnemyDataBase:
    pass

class Enemy:
    def __init__(self, cur, idx) -> None:
        self.cur = cur
        self.idx = idx

    def get_status(self):
        """name text,
                hitpoint int,
                strength int,
                defence int,
                magicpower int,
                critical int,
                exp int,"""

        status = self.cur.execute(
            "SELECT hitpoint, strength, defence, magicpower, critical FROM enemies_master WHERE id=?", (self.idx, )).fetchall()[0]
        return status

    def get_abilities(self):
        abilities = []
        # self.cur.execute(
        #     """
        #     SELECT ability.name, ability.description, ability.count, ability.target, ability.type, ability.fixed_value, ability.value
        #     FROM ability
        #     JOIN enemies_master
        #     WHERE ability.id=enemies_master.ability_id
        #     """
        # ).fetchall()
        return abilities

    def get_exp(self):
        exp = self.cur.execute("SELECT exp FROM enemies_master WHERE id=?", (self.idx,)).fetchone()[0]
        return exp

    def get_name(self):
        return self.cur.execute("SELECT name FROM enemies_master WHERE id=?", (self.idx,)).fetchone()[0]

    def get_entity(self):
        entity = ActorEntity(*self.get_status())
        entity.set_abilities(self.get_abilities())
        return entity

class EnemyFactory:
    def __init__(self, cur) -> None:
        self.cur = cur

    def create(self, idx):
        return Enemy(self.cur, idx)



con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS quests_master (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                description text,
                enemy_id int,
                defficulty int,
                money int,
                rank_exp int
            )""")
cur.execute("""INSERT INTO quests_master(name, description, enemy_id, defficulty, money, rank_exp)
            VALUES ('ゴブリン討伐', 'ゴブリンを討伐せよ', 1, 0, 10, 10)""")
cur.execute("""INSERT INTO quests_master(name, description, enemy_id, defficulty, money, rank_exp)
            VALUES ('ドラゴン討伐', 'ドラゴンを討伐せよ', 2, 1, 20, 20)""")

cur.execute("""
            CREATE TABLE IF NOT EXISTS enemies_master (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
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
cur.execute("""
            INSERT INTO enemies_master(name, hitpoint, strength, defence, magicpower, critical, exp, ability_id)
            VALUES ('ゴブリン', 24, 8, 4, 0, 0, 10, 1)
            """)

quests = QuestsDataBase(cur)
idx = quests.select()
quest: QuestEntity = quests.get_entity(idx)

enemy_factory = EnemyFactory(cur)
enemy = enemy_factory.create(quest.enemy_id)
enemy_entity = enemy.get_entity()
print(enemy.get_name(), enemy_entity.strength)

con.commit()