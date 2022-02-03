import sqlite3


con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS user (id int, name text)")
cur.execute("INSERT INTO user VALUES (0, 'ボブ')")

for row in cur.execute("SELECT * FROM user"):
    print(row)