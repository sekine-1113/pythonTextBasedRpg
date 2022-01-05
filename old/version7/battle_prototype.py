
from version7.actor import ActorEntity


class Battle:
    def __init__(self, player, enemy) -> None:
        self.player: ActorEntity = player
        self.enemy: ActorEntity = enemy

    def turn_clock(self):
        player_action = self.player_turn()
        if player_action == -1:
            return -1
        elif player_action == -2:
            return self.turn_clock()
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
        if quantity == -1:
            return -2
        if ability.type_ == 0:
            damage = self.enemy.take_damage(quantity)
            print(damage, "ダメージを与えた!")
        elif ability.type_ == 1:
            heal = self.player.take_heal(quantity)
            print(heal, "回復した!")
        elif ability.type_ == 2:
            damage = self.enemy.take_damage(quantity)
            print(damage, "ダメージを与えた!")
        return 0

    def enemy_turn(self):
        ability = self.enemy.enemy_ai.select()
        idx = self.enemy.enemy_ai.get_index(ability)
        quantity = self.enemy.execute(idx)
        if ability.type_ == 0:
            damage = self.player.take_damage(quantity)
            print(damage, "ダメージ受けた!")
        elif ability.type_ == 1:
            heal = self.enemy.take_heal(quantity)
            print(heal, "回復した!")
        elif ability.type_ == 2:
            damage = self.enemy.take_damage(quantity)
            print(damage, "ダメージ受けた!")
        return 0
