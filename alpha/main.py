
class HitPoint:
    def __init__(self, value: int) -> None:
        assert isinstance(value, int)
        self.value = value
        self.max_value = value
        self.min_value = 0


class MagicPower:
    def __init__(self, value: int) -> None:
        assert isinstance(value, int)
        self.value = value
        self.max_value = value
        self.min_value = 0

class Stats:
    def __init__(self, hit_point: HitPoint, magic_power: MagicPower) -> None:
        assert isinstance(hit_point, HitPoint)
        assert isinstance(magic_power, MagicPower)
        self.hit_point = hit_point
        self.magic_power = magic_power

class Player:
    def __init__(self, name: str, stats: Stats) -> None:
        assert isinstance(name, str)
        assert isinstance(stats, Stats)
        self.name = name
        self.stats = stats


    def heal(self):
        print(self.stats.hit_point.max_value - self.stats.hit_point.value)
        self.stats.hit_point.value = self.stats.hit_point.max_value

    def recieve_damage(self, damage):
        self.stats.hit_point.value -= damage


def main():
    player: Player = Player(name="アリス",
        stats=Stats(
            hit_point=HitPoint(1200),
            magic_power=MagicPower(300)
        )
    )
    print(player.stats.hit_point.value)
    player.recieve_damage(1000)
    print(player.stats.hit_point.value)
    player.heal()
    print(player.stats.hit_point.value)
    return 0


if __name__ == "__main__":
    main()