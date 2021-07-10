from character.player import Player
from character.status.rank import Rank
from item.money import Money

player = Player("アリス")
print(player)
print(vars(player))

player.set_money(Money(9999, 0, 0))
player.set_rank(Rank(20, 1, 1))

print(player)
print(vars(player))