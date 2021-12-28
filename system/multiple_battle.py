from copy import deepcopy
from random import randint


class Stats:
    def __init__(self, lv, hp, st, df):
        self.lv = lv
        self.hp = hp
        self.st = st
        self.df = df

    def __repr__(self):
        return f"{self.hp}"


class Actor:
    def __init__(self, name, stats: Stats):
        self.name = name
        self.stats = stats

    def do_attack(self):
        r = randint(0, 4)
        damage = self.stats.st + r
        return damage

    def recv_damage(self, damage):
        damage -= int(self.stats.df/2)
        self.stats.hp -= damage
        return damage

    def is_dead(self):
        return self.stats.hp <= 0

    def __repr__(self):
        return repr(self.stats)


player = Actor("Player",
            Stats(1,32,12,8))
friendA = Actor("FriendA",
            Stats(1,36,8,4))
enemy = Actor("EnemyA",
            Stats(1,48,8,4))
enemyB = Actor("EnemyB",
            Stats(1,24,4,4))

class Party:
    def __init__(self):
        self.member: list[Actor] = []

    def add(self, member):
        self.member.append(member)

party = Party()
party.add(player)
party.add(friendA)
friendB = deepcopy(friendA)
friendB.name = "FriendB"
party.add(friendB)
partyB = Party()
partyB.add(enemy)
partyB.add(enemyB)
turn = 0
loop=True
while loop:
    turn += 1
    print("Turn", turn)
    for memb in party.member:
        damage = memb.do_attack()
        target_index = randint(0, len(partyB.member)-1)
        if memb.name == "Player":
            for i,target in enumerate(partyB.member):
                print(i,target.name)
            target_index = int(input("> "))
        partyB.member[target_index].recv_damage(damage)
        print(memb.name, "->",
            partyB.member[target_index].name,
            damage)
        if partyB.member[target_index].is_dead():
            print(partyB.member[target_index].name,"killed")
            del partyB.member[target_index]
            if not partyB.member:
                print("You win!")
                loop=False
                break
    for memb in partyB.member:
        damage = memb.do_attack()
        target = randint(0, len(party.member)-1)
        party.member[target].recv_damage(damage)
        print(memb.name, "->",
            party.member[target].name,
            damage)
        if party.member[target].is_dead():
            print(party.member[target].name, "is dead")
            del party.member[target]
            if not party.member:
                print("You lose!")
                loop=False
                break