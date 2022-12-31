
def set_attrs(__obj, __dict, **kwargs):
    for key, value in __dict.items():
        setattr(__obj, key, value)
    for key, value in kwargs.items():
        setattr(__obj, key, value)
    return __obj


class Memento:
    def __init__(self) -> None:
        pass

class Player:
    def __init__(self, name, stats) -> None:
        self.name = name
        self.stats = stats

    def create_memento(self):
        return set_attrs(Memento(), vars(self))

    def set_memento(self, memento):
        new_instance = Player(None, None)
        for key, value in vars(memento).items():
            setattr(new_instance, key, value)
        return new_instance

    def rename(self, new_name):
        return Player(new_name, self.stats)

    def update_stats(self, key, value):
        new_stats = self.stats.copy()
        new_stats[key] = value
        return Player(self.name, new_stats)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: '{self.name}'>"


class Game:
    def __init__(self) -> None:
        self.memento = []

    def main(self):
        gameloop = True
        p = Player("PlayerName", {"HP": 300, "ATK": 100})
        self.memento.append(p.create_memento())
        while gameloop:
            print(p)
            cmd = int(input("[1:Rename (2:Change Status) 3:Restore 0:Exit] > "))
            if cmd == 0:
                gameloop = False
                break
            elif cmd == 1:
                new_name = input("New Name > ")
                p = p.rename(new_name)
                self.memento.append(p.create_memento())
            elif cmd == 2:
                new_stats_k = input("Stats Name > ")
                new_stats_v = int(input("Stats Value > "))
                p = p.update_stats(new_stats_k, new_stats_v)
                self.memento.append(p.create_memento())
            elif cmd == 3:
                if len(self.memento) >= 2:
                    self.memento.pop()
                elif len(self.memento) <= 0:
                    print("newest status")
                    pass
                else:
                    memento = self.memento.pop()
                    p = p.set_memento(memento)

Game().main()