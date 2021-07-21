import json

from character.player import Player
from character.role import Role
from character.status.rank import Rank
from character.status.exp import Exp
from item.money import Money


path = r"D:\myscript\games\cui\textbasedrpg\data\user.json"

with open(path, "r", encoding="UTF-8") as f:
    user = json.load(f)


player = Player(
    user["name"],
    Rank(**user["rank"]),
    Money(**user["money"]),
    user["item"],
    user["role"]
)


print(player.rank.calc_rank())
player.rank.next_rank_exp(player.rank.calc_rank())
e = player.rank.diff_next_rank_exp()
player.rank.gain_exp(e)
print(player.rank.calc_rank())


