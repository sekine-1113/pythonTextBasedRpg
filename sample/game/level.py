import random


XP = 30000

class PlayerXP:
    def __init__(self, xp=0) -> None:
        self.value = max(0, xp)

    def gain_xp(self, xp):
        return PlayerXP(self.value + xp)

    def get_level(self):
        return min(self.value // XP + 1, 100)

    def get_next_xp(self):
        return XP - self.value % XP if self.get_level()==100 else 0

    def __repr__(self) -> str:
        return str(self.value)


xp = PlayerXP(0)
next_xp = xp.get_next_xp()
level = xp.get_level()

for i in range(200):
    print(level, xp, next_xp)
    if level == 100:
        break
    xp = xp.gain_xp(random.randint(20000, 30000))

    next_xp = xp.get_next_xp()
    level = xp.get_level()



