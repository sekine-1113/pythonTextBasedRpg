
class Actor:
    ability_list = []

    def __init__(self, name, abilities=[], level=1) -> None:
        self.name = name
        self.abilities: list = abilities
        self.level = level

    def set_ability(self, ability):
        if ability in self.abilities:
            print(f"{ability}はすでに覚えています")
            return
        if ability not in self.ability_list:
            print(f"{ability}は覚えられません")
            return
        self.abilities.append(ability)
        if len(self.abilities) > 4:
            del self.abilities[0]

    def set_default_ability(self):
        for ability in self.ability_list:
            if ability[0] <= self.level:
                self.set_ability(ability)
            else:
                break

    def get_ability(self):
        for ability in self.abilities:
            print(ability[1], end=",")
        print()


class Player(Actor):
    ability_list = [
        [1, 'こうげき'],
        [1, 'ぼうぎょ'],
        [3, 'かいふく'],
        [5, 'にげる']
    ]

    def __init__(self, name, abilities, level=1) -> None:
        super().__init__(name, abilities, level)



if __name__ == "__main__":
    player = Player("アリス", [], 5)
    player.set_default_ability()
    player.get_ability()
    player.set_ability('ねむる')
    player.get_ability()
    player.set_ability('にげる')
    player.get_ability()
    player.set_ability('にげる')
    player.get_ability()
