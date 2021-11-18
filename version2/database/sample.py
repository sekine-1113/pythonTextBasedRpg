
import sqlite3

DEBUG = True

filename = ":memory:" if DEBUG else "sample.db"

con = sqlite3.connect(filename)
cur = con.cursor()

cur.execute("CREATE TABLE lang (name, first_appeared)")

cur.execute("INSERT INTO lang VALUES (?, ?)", ("C", 1972))

lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]

cur.executemany("INSERT INTO lang VALUES (?, ?)", lang_list)
cur.execute("SELECT * FROM lang")
print(cur.fetchall())
cur.execute("SELECT * FROM lang WHERE first_appeared=:year", {"year": 1972})
print(cur.fetchall())
cur.execute("SELECT * FROM lang WHERE first_appeared>:year", {"year": 1972})
print(cur.fetchall())
con.close()
