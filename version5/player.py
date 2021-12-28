

class PlayerMaster:
    def __init__(self, name) -> None:
        self.name = name

    def set_status(self, money, class_id):
        self.money = money
        self.class_id = class_id

    def get_status(self):
        return (self.money, self.class_id)

    def __repr__(self) -> str:
        return self.name



class PlayerFactory:
    def __init__(self) -> None:
        pass

    def create(self):
        pm = PlayerMaster("アリス")
        pm.set_status(0, 0)
        return pm


class PlayerList:
    def __init__(self) -> None:
        self.players = []

    def add(self, player: PlayerMaster):
        self.players.append(player)

    def get(self, player):
        return self.players[self.players.index(player)]


if __name__ == "__main__":
    pl = PlayerList()
    pf = PlayerFactory()
    player = pf.create()
    pl.add(player)

    print(pl.get(player))