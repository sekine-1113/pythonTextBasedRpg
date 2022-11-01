AUTO_SAVE = True

import random
from pprint import pprint

from util.gentoken import (
    create_id,
    create_token,
    create_random_password,
    get_password,
    confirm_password,
    hased
)

data_dict = {}
jpn = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
for _ in range(10):
    spell = "".join(random.choices(jpn, k=32))
    print("ふっかつのじゅもん")
    print(spell)
    _data_hashed = hased(spell)
    data_dict[_data_hashed] = {"name":"ゆうしゃ", "stats": {"HP":200, "MP":0}}
pprint(data_dict, width=120)

