
class Player:
    def __init__(self, idx, name, money, class_id) -> None:
        self.idx = idx
        self.name = name
        self.money = money
        self.class_id = class_id

    def __repr__(self) -> str:
        return f"[#{self.idx}] {self.name} {self.money}G (#{self.class_id})"

class Enemy:
    def __init__(self, idx, name, money) -> None:
        self.idx = idx
        self.name = name
        self.money = money

    def __repr__(self) -> str:
        return f"[#{self.idx}] {self.name} {self.money}G"


class ActorFactory:
    def __init__(self, actor_class) -> None:
        self.actor_class = actor_class

    def create(self):
        if issubclass(self.actor_class, Player):
            return self.actor_class(1, "アリス", 0, 1)
        else:
            return self.actor_class(1, "ゴブリン", 0)


player_factory = ActorFactory(Player)
player = player_factory.create()
enemy_factory = ActorFactory(Enemy)
enemy = enemy_factory.create()
print(player)
print(enemy)
