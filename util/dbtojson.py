import sqlite3
from pprint import pprint


class DataBase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()


    def test(self):
        self.cur.execute("CREATE TABLE MyTable (id INTEGER, message TEXT)")
        for i in range(3):
            self.cur.execute(f"INSERT INTO MyTable VALUES ({i}, 'myTest{i}')")
        self.cur.execute("SELECT * FROM MyTable")
        data = self.cur.fetchone()

        json = {key: data[key] for key in data.keys()}
        pprint(json)
        self.conn.commit()
        self.cur.close()


if __name__ == "__main__":
    DataBase()