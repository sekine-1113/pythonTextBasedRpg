
class Battle:
    def __init__(self, player, enemy) -> None:
        self.turn = 0
        self.player_win = False
        self.player = player
        self.enemy = enemy

    def turn_clock(self):
        self.turn += 1
        print(self.turn)
        player_action = self.player_turn()
        if player_action == -1:
            return -1

        if self.enemy.is_dead():
            return True

        self.enemy_turn()
        if self.player.is_dead():
            return False

        return self.turn_clock()

    def player_turn(self):
        idx = self.player.ability_select()
        if idx < 0:
            return -1
        ability = self.player.get_ability(idx)
        quantity = self.player.execute(idx)
        print(ability.name)
        if ability.type_ == 0:
            self.enemy.take_damage(quantity)
        elif ability.type_ == 1:
            self.player.take_heal(quantity)
        return 0

    def enemy_turn(self):
        return 0
