import os, sys
sys.path.append(os.path.dirname(sys.argv[0]))

from role import Role


class Wizard(Role):
    def __init__(self, level, hitpoint, magicpower,
                strength, defence, intelligence,
                luck, exp, weapon, good_weapon,
                armor, accessory1, accessory2) -> None:
        self.name = "ウィザード"
        super().__init__(self.name, level, hitpoint, magicpower,
                        strength, defence, intelligence,
                        luck, exp, weapon, good_weapon,
                        armor, accessory1, accessory2)



def main():
    wizard = Wizard(1, 1200, 200, 450, 300, 200, 1, 0, None, None, None, None, None)
    print(vars(wizard))


if __name__ == "__main__":
    main()