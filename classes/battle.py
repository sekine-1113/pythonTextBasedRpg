from classes.character import Character


class Battle:
    def __init__(self, ) -> None:
        self.loop = True
        self.isplayerwin = False
        self.heal = True
        self.item = True
        self.escape = True

    def fight(self):
        self.loop = True
        while self.loop:
            # プレイヤーパーティのターン
            # エネミーパーティのターン
            # 勝利判定
            self.loop = False



if __name__ == "__main__":
    player, enemy = Character(), Character()