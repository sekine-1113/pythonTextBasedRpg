

class ConstDict:

    def __init__(self, store_object):
        if not isinstance(store_object, dict):
            raise Exception
        self.__store_object = store_object

    def __setitem__(self, __k, __v) -> None:
        if (__v:=self.__store_object.__getitem__(__k)):
            return
        return self.__store_object.__setitem__(__k, __v)

    def __getitem__(self, __k):
        return self.__store_object.__getitem__(__k)

    def get(self, __k):
        return self.__getitem__(__k)

CONFIG = ConstDict({
    "hoge": "hogehoge"
})

# CONFIG = ConstDict({
#     "GameTitle": "SimpleRPG"
# })


class Actor:
    def __init__(self, name, hp, power, exp, is_player) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.exp = exp
        self.is_player = is_player

    def show(self):
        print(f"Name: {self.name}")
        print(f"HP : {self.hp:3}")
        if self.is_player:
            print(f"STR: {self.power:3}")
            print(f"EXP: {self.exp:3}")


def main():
    player = Actor("Player", 30, 8, 0, True)
    enemy = Actor("Enemy", 24, 6, 4, False)

    print(f"Welcom to {CONFIG['GameTitle']}!")
    gameloop = input("[1] Start [0] Exit > ")

    if (not gameloop):
        print("Bye!")
        return

    player.show()
    enemy.show()


# main()

