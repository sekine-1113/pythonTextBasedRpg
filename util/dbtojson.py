import sqlite3
from pprint import pprint


conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("CREATE TABLE MyTable (id INTEGER, message TEXT)")
for i in range(3):
    cur.execute(f"INSERT INTO MyTable VALUES ({i}, 'myTest{i}')")
cur.execute("SELECT * FROM MyTable")
data = cur.fetchone()

json = {key: data[key] for key in data.keys()}
#for key in data.keys():
#    json[key] = data[key]
pprint(json)
conn.commit()
cur.close()
