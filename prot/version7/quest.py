from settings import Input


class QuestEntity:
    def __init__(self, name: str, desc: str, enemy_id: int, deff: int, money: int, rank_exp: int) -> None:
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

    def select(self) -> int:
        quests = self.cur.execute("SELECT id, name FROM quests_master").fetchall()
        for quest in quests:
            print(*quest)
        return Input.integer()

    def filtered_select(self) -> int:
        print("難易度")
        print("1: Easy")
        print("2: Middle")
        print("3: Difficult")
        print("0: もどる")
        diff = Input.integer()
        if diff == 0:
            return -1
        quests = self.cur.execute("SELECT id, name FROM quests_master WHERE difficulty=?", (diff, ))
        for quest in quests:
            print(*quest)
        return Input.integer()

    def get_entity(self, idx: int) -> QuestEntity:
        quest = self.cur.execute(
            "SELECT name, description, enemy_id, difficulty, money, rank_exp FROM quests_master WHERE id=?",
            (idx, )
        ).fetchone()
        return QuestEntity(*quest)
