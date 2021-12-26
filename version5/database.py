import sqlite3

from constant import DATABASE_FILE_PATH



def create_table(table_name, values):
    return f"CREATE TABLE IF NOT EXISTS {table_name} {values}"

def insert_table(table_name, values):
    return f"INSERT INTO {table_name} VALUES {values}"

def select_table(table_name, coulmn="*", join=None, where=None):
    sql =  f"SELECT {coulmn} FROM {table_name}"
    if join: sql += f" JOIN {join}"
    if where: sql += f" WHERE {where}"
    return sql


def main():
    con = sqlite3.connect(DATABASE_FILE_PATH)
    cur = con.cursor()

    cur.execute(create_table("player_master", "(id int PRYMARY KEY, name text)"))
    cur.execute(insert_table("player_master", "(0, 'アリス')"))
    pid, pname = cur.execute(select_table("player_master", where="id=0")).fetchone()
    print(f"{pid=} {pname=}")

    cur.execute(create_table("player_information", "(id int, money int, class_id int)"))
    cur.execute(insert_table("player_information", "(0, 0, 0)"))
    pmoney, pclass_id = cur.execute(select_table("player_information", "money, class_id", where="id={}".format(pid))).fetchone()
    print(f"{pmoney=} {pclass_id=}")

    cur.execute(create_table("player_classes_exp", "(id int, class_id int, exp int)"))
    cur.execute(insert_table("player_classes_exp", "(0, 0, 300)"))
    pexp = cur.execute(select_table("player_classes_exp", "exp", where=f"id={pid} AND class_id={pclass_id}")).fetchone()[0]
    print(f"{pexp=}")

    cur.execute(create_table("classes_status", "(id int, exp int, level int)"))
    cur.execute(insert_table("classes_status", "(0, 0, 0)"))
    cur.execute(insert_table("classes_status", "(1, 30, 1)"))
    cur.execute(insert_table("classes_status", "(2, 100, 2)"))
    cur.execute(insert_table("classes_status", "(3, 200, 3)"))
    cur.execute(insert_table("classes_status", "(4, 300, 4)"))
    cur.execute("UPDATE classes_status SET exp=350 WHERE id=4")
    plevel = cur.execute(select_table("classes_status", "MAX(level)", where=f"exp<={pexp}")).fetchone()[0]
    print(f"{plevel=}")

    cur.execute("DROP TABLE player_master")
    cur.execute("DROP TABLE player_information")
    cur.execute("DROP TABLE player_classes_exp")
    cur.execute("DROP TABLE classes_status")
    con.commit()
    cur.close()
    con.close()


main()