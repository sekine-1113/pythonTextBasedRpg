import random


class Actor:
    def __init__(self, name, level, hit_point, strength, defense) -> None:
        self.name = name
        self.disp_name = name
        self.level = level
        self.max_hit_point = hit_point
        self.hit_point = hit_point
        self.strength = strength
        self.defense = defense

    def attack(self, target):
        damage = self.strength + random.randint(0, int(self.strength / 4))
        at_damage = target.receive(damage)
        if at_damage > 0:
            print(f"{at_damage}ダメージあたえた!")
        else:
            print("Miss!")

    def receive(self, damage):
        damage = damage - self.defense + random.randint(0, 1)
        damage = abs(damage)
        if damage > 0:
            print(f"{self.disp_name}は{damage}ダメージを受けた")
        self.hit_point -= damage
        if self.hit_point < 0:
            self.hit_point = 0
        return damage

    def reset(self):
        self.hit_point = self.max_hit_point

    def is_dead(self):
        return self.hit_point <= 0

    def level_up(self):
        self.level += 1
        self.max_hit_point += 2
        self.reset()
        self.strength += 1
        self.defense += 1
        self.show_stats()

    def show_stats(self):
        print(f"{self.disp_name}(Lv:{self.level}) - HP:{self.hit_point}/{self.max_hit_point} STR:{self.strength} DEF:{self.defense}")


class Party:
    def __init__(self, default=None) -> None:
        self.members = default or []

    def add(self, member):
        if len(self.members) > 25:
            raise Exception
        i_list = []
        for i, _member in enumerate(self.members):
            if _member.name == member.name:
                i_list.append(i)
                continue
        for i in i_list:
            self.members[i].disp_name = self.members[i].name + chr(ord("A")+i)
        member.disp_name = member.name + chr(ord("A")+len(i_list))
        self.members.append(member)

    def is_over(self):
        return all([member.is_dead() for member in self.members])

    def alive_members(self, idx=True):
        members = []
        for i, member in enumerate(self.members):
            if member.is_dead():
                continue
            if idx:
                members.append(i)
            else:
                members.append(member)
        return members


def battle(player_party, enemy_party):
    pp: Party = player_party
    ep: Party = enemy_party
    players: list[Actor] = pp.members
    enemies: list[Actor] = ep.members

    for enemy in enemies:
        print(f"{enemy.disp_name}があらわれた!")
    for player in players:
        player.show_stats()
    for enemy in enemies:
        enemy.show_stats()

    while True:
        for player in players:
            if player.is_dead():
                continue

            if len(ep.alive_members(False)) > 1:
                t = ",".join(map(str, ep.alive_members()))
                target = int(input(f"({t})> "))
            else:
                target = ep.alive_members()[0]
            print(f"{player.disp_name}のこうげき!")
            player.attack(enemies[target])

            if enemies[target].is_dead():
                print(enemies[target].disp_name, "を倒した!")

        if ep.is_over():
            if len(ep.members) > 1:
                print("まもののむれをやっつけた!")
            else:
                print(f"{enemies[target].disp_name}をやっつけた!")
            break

        for enemy in enemies:
            if enemy.is_dead():
                continue
            target = random.randint(0, len(players)-1)

            print(f"{enemy.disp_name}のこうげき!")
            enemy.attack(players[target])

        if pp.is_over():
            print("たおされた...")
            break

        for player in players:
            player.show_stats()

        for enemy in enemies:
            enemy.show_stats()

        print("="*20)

    for player in players:
        player.reset()
        player.show_stats()
    for enemy in enemies:
        enemy.reset()
        enemy.show_stats()


def main():
    pp = Party([Actor("アリス", 1, 12, 6, 4)])
    ep = Party()
    for _ in range(2):
        ep.add(Actor("スライム", 1, 8, 5, 2))
    battle(pp, ep)


main()