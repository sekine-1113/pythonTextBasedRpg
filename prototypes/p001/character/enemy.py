
class Enemy:

    def __init__(self, name) -> None:
        self.name = name
        self.money = None
        self.item = None
        self.role = None


if __name__ == "__main__":
    from character.role import Role
    enemy = Enemy("スライムくん")
    enemy.role = Role()
    enemy.role.name = "スライム"
    print(enemy.name)
    print(enemy.role.name)