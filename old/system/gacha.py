import sqlite3
import random

from enum import IntEnum
from pprint import pprint


class Rarerity(IntEnum):
    N = 0
    R = 1
    SR = 2
    SSR = 3

rares = [Rarerity.R, Rarerity.SR, Rarerity.SSR]
prob = [70, 20, 10]

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS equipments (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, rare int)")
values = []
for i in range(100):
    rare = random.choices(rares, weights=prob)[0]
    name = rare.name+str(i)
    values.append((name, rare.value))


cur.executemany("INSERT INTO equipments(name, rare) VALUES (?, ?)", values)
sql = "SELECT * FROM equipments WHERE rare>0"
content = cur.execute(sql).fetchall()
print(content)
weights = []
for item in content:
    for i in range(3):
        if rares[i] == item[2]:
            weights.append(1/rares[i].value)
pprint(random.choices(content, weights=weights, k=10))