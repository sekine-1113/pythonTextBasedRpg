import random


class Actor:
    def __init__(self, name, level, hit_point, strength, defense) -> None:
        self.name = name
        self.level = level
        self.max_hit_point = hit_point
        self.hit_point = hit_point
        self.strength = strength
        self.defense = defense

    def attack(self, target):
        damage = self.strength + random.randint(0, int(self.strength / 4))
        at_damage = target.receive(damage)
        print(f"{at_damage}ダメージあたえた!")

    def receive(self, damage):
        damage = damage - self.defense + random.randint(0, 1)
        damage = abs(damage)
        print(f"{self.name}は{damage}ダメージを受けた")
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
        print(f"{self.name}(Lv:{self.level}) - HP:{self.hit_point}/{self.max_hit_point} STR:{self.strength} DEF:{self.defense}")



class Party:
    def __init__(self) -> None:
        self.members = []

    def add(self, member):
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



class BattleMember:
    def __init__(self, pp, ep) -> None:
        self.player_party: Party = pp
        self.enemy_party: Party = ep


def battle(member: BattleMember):
    pp = member.player_party
    ep = member.enemy_party
    if member is not None:
        players = pp.members
        enemies = ep.members

    for enemy in enemies:
        print(f"{enemy.name}があらわれた!")
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
                target = 0
            player.attack(enemies[target])

            if enemies[target].is_dead():
                print(enemies[target].name, "を倒した!")

        if ep.is_over():
            break

        for enemy in enemies:
            if enemy.is_dead():
                continue
            target = random.randint(0, len(players)-1)
            enemy.attack(players[target])

        if pp.is_over():
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

    return member

def main():
    pp = Party()
    pp.add( Actor("アリス", 1, 12, 6, 3))
    ep = Party()
    ep.add(Actor("スライムA", 1, 8, 3, 1))
    ep.add(Actor("スライムB", 1, 8, 3, 1))
    members = BattleMember(pp, ep)
    battle(members)


main()