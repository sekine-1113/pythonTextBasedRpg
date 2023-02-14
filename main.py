

def next_int(prompt="> "):
    try:
        return int(input(prompt))
    except Exception:
        return next_int(prompt)

class Actor:
    def __init__(self, name, hitpoint, strength, defense, exp, money) -> None:
        self.name = name
        self.hitpoint = hitpoint
        self.strength = strength
        self.defense = defense
        self.exp = exp
        self.money = money

    def copy(self):
        return Actor(**self.__dict__)

class DummyActor(Actor):
    def __init__(self) -> None:
        super().__init__(None, None, None, None, None, None)


class Quest:
    def __init__(self, name, actor) -> None:
        self.name = name
        self.actor = actor

    def __repr__(self) -> str:
        return self.name


quest_list = [
    Quest("もどる", DummyActor()),
    Quest("スライム", Actor("スライム", 800, 450, 300, 100, 20)),
    Quest("ゴブリン", Actor("ゴブリン", 1200, 600, 450, 200, 60)),
    Quest("ドラゴン", Actor("ドラゴン", 1800, 900, 600, 300, 120)),
]

player = Actor("", 1200, 800, 500, 0, 0)

scene_id = 0
while True:
    if scene_id == 0:
        print("ようこそ, Python RPG へ!")
        idx = next_int("1: はじめる\n0: やめる\n> ")
        if idx == 1:
            if player.name == "":
                player_name = input("あなたの名前を入力してください：")
                player.name = player_name
            scene_id = 2
        else:
            break

    elif scene_id == 2:
        print("0:タイトルへもどる")
        print("1:クエスト")
        print("2:ショップ")
        print("3:ステータス")
        scene_id = next_int()
        if scene_id == 2:
            scene_id = 4

    elif scene_id == 3:
        print(player.name)
        print(player.hitpoint)
        scene_id = 2

    elif scene_id == 4:
        print("ショップへようこそ!")
        scene_id = 2

    elif scene_id == 1:
        print("クエスト選択してください")
        for i, quest_name in enumerate(quest_list):
            print(i, quest_name)
        enemy_idx = next_int()
        if enemy_idx == 0:
            scene_id = 0
        else:
            scene_id = 5
    elif scene_id == 5:
        player_copy = player.copy()
        enemy = quest_list[enemy_idx].actor.copy()
        print(enemy.name, "が現れた!")
        while True:
            print(f"{enemy.name}[HP:{enemy.hitpoint}]")
            print(f"{player.name}[HP:{player.hitpoint}]はどうする?")
            for i, command in enumerate(["にげる", "こうげき"]):
                print(i, command)
            action_id = next_int()
            if action_id == 0:
                scene_id = 1
                break
            print(f"{player.name}のこうげき!")
            damage = player.strength ** 2 / enemy.defense % 65535
            enemy.hitpoint -= damage
            print(f"{damage}のダメージをあたえた!")
            if enemy.hitpoint <= 0:
                print(f"{enemy.name}をたおした!")
                print(f"{enemy.exp}EXPを獲得!")
                print(f"{enemy.money}Gを獲得!")
                player = player_copy
                player.exp += enemy.exp
                player.money += enemy.money
                scene_id = 1
                break

            print(f"{enemy.name}のこうげき!")
            damage = enemy.strength ** 2 / player.defense % 65535
            player.hitpoint -= damage
            print(f"{damage}のダメージをくらった!")
            if player.hitpoint <= 0:
                print(f"{player.name}はしんでしまった!")
                player = player_copy
                scene_id = 1
                break
        scene_id = 1

    else:
        break


if __name__ == "__main__":
    print(__name__)