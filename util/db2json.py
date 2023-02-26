import sqlite3


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
        data = self.cur.fetchall()
        data = map(self.to_json, data)
        self.conn.commit()
        self.cur.close()


    def to_json(self, data):
        json = {key: data[key] for key in data.keys()}
        return json


if __name__ == "__main__":
    DataBase().test()