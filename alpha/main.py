
class VariableStat:
    def __init__(self, value: int) -> None:
        assert isinstance(value, int)
        self.value: int = value
        self.max_value: int = value
        self.min_value: int = 0

    def add(self, value: int) -> None:
        assert isinstance(value, int)
        self.value += value
        self.max_value = self.value

    def decrease(self, value: int) -> None:
        assert isinstance(value, int)
        self.value = max(self.value-value, self.min_value)

    def recover(self, value: int) -> None:
        assert isinstance(value, int)
        self.value = min(self.value+value, self.max_value)

    def restore(self) -> None:
        self.value = self.max_value


class HitPoint(VariableStat):
    pass


class MagicPower(VariableStat):
    pass


class Strength(VariableStat):
    pass


class Stats:
    def __init__(self, hit_point: HitPoint, magic_power: MagicPower, strength: Strength) -> None:
        assert isinstance(hit_point, HitPoint)
        assert isinstance(magic_power, MagicPower)
        assert isinstance(strength, Strength)
        self.hit_point: HitPoint = hit_point
        self.magic_power: MagicPower = magic_power
        self.strength: Strength = strength


class Money:
    def __init__(self, value: int) -> None:
        assert isinstance(value, int)
        self.value: int = value


class Skill:
    def __init__(self, name: str, mp: int) -> None:
        self.name: str = name
        self.mp: int = mp


class Job:
    def __init__(self, stats: Stats) -> None:
        self.stats: Stats = stats
        self.skills: list[Skill] = [Skill("メラ", 50), Skill("メラミ", 150)]


class Command:
    def __init__(self, cmd) -> None:
        self.cmd = cmd

    def execute(self):
        self.cmd()
        return True


class RunCommand:
    def execute(self):
        return False

class Player:
    def __init__(self, name: str, job: Job, money: Money) -> None:
        assert isinstance(name, str)
        assert isinstance(job, Job)
        assert isinstance(money, Money)
        self.name: str = name
        self.job: Job = job
        self.money: Money = money

    def choose_action(self):
        idx = int(input("#1 attack, #2 use skill #0 run> "))
        action = [
            RunCommand(),
            Command(self.attack),
            Command(lambda: self.use_skill(skill_idx=0))
        ]
        return action[idx]

    def attack(self):
        return self.job.stats.strength

    def use_skill(self, skill_idx: int) -> None:
        if not self.__has_skill(skill_idx):
            print("スキルを覚えていない!")
            return

        using_skill: Skill = self.job.skills[skill_idx]
        if self.job.stats.magic_power.value < using_skill.mp:
            print("MPが足りなかった!")
            return

        self.job.stats.magic_power.decrease(using_skill.mp)
        print("using", using_skill.name, end=" ")
        print("mp", using_skill.mp)
        damage = 100
        return damage

    def __has_skill(self, skill_idx: int) -> bool:
        return len(self.job.skills) > skill_idx

    def is_dead(self) -> bool:
        return self.job.stats.hit_point.value <= 0



def main():
    player: Player = Player(name="アリス",
        job=Job(
            stats=Stats(
                hit_point=HitPoint(1200),
                magic_power=MagicPower(300),
                strength=Strength(500)
            ),
        ),
        money=Money(0),
    )

    enemy: Player = Player(name="スライム",
        job=Job(
            stats=Stats(
                hit_point=HitPoint(800),
                magic_power=MagicPower(100),
                strength=Strength(400)
            ),
        ),
        money=Money(300),
    )

    while True:
        player_action = player.choose_action()
        if not player_action.execute():
            break
        print(player.name, "attack!")
        print(player.job.stats.strength.value)
        enemy.job.stats.hit_point.decrease(player.job.stats.strength.value)
        if enemy.is_dead():
            break

        print(enemy.name, "attack!")
        print(enemy.job.stats.strength.value)
        player.job.stats.hit_point.decrease(enemy.job.stats.strength.value)
        if player.is_dead():
            break

    return 0


if __name__ == "__main__":
    main()