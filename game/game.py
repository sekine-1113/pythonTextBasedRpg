DEBUG = True

class Actor:
    def __init__(self, name, level, hit_point, magic_power, strength, defence, xp, money):
        print_message("creating Actor object...")
        self.name = name
        self.level = level
        self.hit_point = hit_point
        self.magic_power = magic_power
        self.strength = strength
        self.defence = defence
        self.xp = xp
        self.money = money
        self.inventory = []

    def set_render(self, render):
        self.render = render

    def get_vars(self):
        print_message("called: Actor.get_vars")
        return self.__dict__

    def attack(self, skill):
        if hasattr(self, "render"):
            self.render(self, skill)
        else:
            Render.attack(self, skill)
        d = AmountCalc.damage(self, skill)
        print_message("actor.attack")
        print("damage is", d)
        return d

    def recieve(self, source, skill):
        Render.recieve(self, skill)
        d = AmountCalc.damage(source, skill)
        self.hit_point -= d
        # 副作用

        print("HP:", self.hit_point)

def print_message(msg, loginfo="INFO"):
    if not DEBUG:
        return
    print(f"[{loginfo}]{msg}", flush=True)

class Skill:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Render:  # 名前空間
    def __init__(self):
        pass
    @classmethod
    def print_message(self, message):
        print(message)
    @classmethod
    def print_actor(self, actor):
        if not isinstance(actor, Actor):
            raise TypeError
        print(actor.name)
    @classmethod
    def attack(self, actor, skill):
        print(actor.name, skill.name)
    @classmethod
    def recieve(self, actor, skill):
        print(actor.name, skill.name)

class AmountCalc:
    @classmethod
    def damage(self, actor, skill):
        damage_amount = actor.strength + skill.amount
        return damage_amount


if __name__ == "__main__":
    actor = Actor("alice", 1, 30, 10, 8, 6, 0, 0)
    print_message("Created Actor")
    print_message(actor.get_vars())
    Render.print_actor(actor)
    skills = [
        Skill("Fire", 10),
        Skill("Ice", 10)
    ]
    using_skill_idx = 1
    skill = skills[using_skill_idx]
    enemy = Actor("slime", 1, 15, 8, 7, 5, 7, 10)
    damage = actor.attack(skill)
    enemy.recieve(actor, skill)