import sqlite3


con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS user (id int, name text, user_id text, class_id int)")
cur.execute("INSERT INTO user VALUES (0, 'Alice', '3gB8re', 0)")
cur.execute("INSERT INTO user VALUES (1, 'Bob', 'gre8', 0)")
cur.execute("INSERT INTO user VALUES (2, 'Sam', 'gar5', 1)")

cur.execute("CREATE TABLE IF NOT EXISTS class (id int, name text, level int, max_level int)")
cur.execute("INSERT INTO class VALUES (0, '勇者', 1, 20)")
cur.execute("INSERT INTO class VALUES (1, '戦士', 1, 20)")
cur.execute("INSERT INTO class VALUES (2, '僧侶', 1, 20)")


for row in cur.execute("""
                    SELECT user.id, user.name, user.user_id,
                        class.id, class.name, class.level, class.max_level
                    FROM user
                    JOIN class
                    ON user.class_id = class.id"""):
    print(row)

con.commit()
cur.close()
con.close()