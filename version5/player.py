

class PlayerStatus:
    def __init__(self, idx, money, class_id, rank_exp) -> None:
        self.idx = idx
        self.money = money
        self.class_id = class_id
        self.rank_exp = rank_exp

    def get_status(self):
        return (self.idx, self.money, self.class_id, self.rank_exp)

    def add_rank_exp(self, exp):
        self.rank_exp += exp

    def set_rank_sql(self, cur):
        cur.execute("UPDATE player_status SET rank_exp={} WHERE id={}".format(self.rank_exp, self.idx))

    def get_rank_sql(self, cur):
        return cur.execute(
            "SELECT MAX(rank_id) FROM rank_master JOIN player_status WHERE player_status.rank_exp >= rank_master.rank_exp AND player_status.id={}".format(self.idx)).fetchone()[0]


class PlayerClassesExp:
    def __init__(self, idx, class_id, class_exp) -> None:
        self.idx = idx
        self.class_id = class_id
        self.class_exp = class_exp

    def get_classes_exp(self):
        return (self.idx, self.class_id, self.class_exp)


class PlayerMaster:
    def __init__(self, idx, name):
        self.idx = idx
        self.name = name
        self.status: PlayerStatus = None
        self.classes_exp: list[PlayerClassesExp] = []

    def get_player(self, cur):
        self.idx, self.name = cur.execute("SELECT id, name FROM player_master WHERE id={}".format(self.idx)).fetchone()
        return self.idx, self.name

    def set_status(self, money, class_id, rank_exp):
        self.status =  PlayerStatus(self.idx, money, class_id, rank_exp)

    def get_status(self):
        return (self.idx,
                self.status.money,
                self.status.class_id,
                self.status.rank_exp)

    def set_class_exp(self, class_id, class_exp):
        self.classes_exp.append(PlayerClassesExp(self.idx, class_id, class_exp))

    def get_class_exp(self, class_id):
        for _class in self.classes_exp:
            if _class.class_id == class_id:
                return _class
        return

    def __repr__(self) -> str:
        return f"{self.name}"


class PlayerFactory:
    def __new__(cls, idx, name) -> PlayerMaster:
        player = PlayerMaster(idx, name)
        return player
        # player.set_class_exp()