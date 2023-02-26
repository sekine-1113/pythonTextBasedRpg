import sqlite3


sql = sqlite3.connect(":memory:")
cur = sql.cursor()

cur.execute("CREATE TABLE users (id INTEGER, name TEXT)")

with open(r"sample\example.sql", "r", encoding="UTF-8") as f:
    insert = f.read()

cur.execute(insert, (1, "Bob"))
cur.execute(insert, (2, "Alice"))


r = cur.execute("SELECT * FROM users").fetchall()
print(r)