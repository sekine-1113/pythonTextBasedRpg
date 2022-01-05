import sqlite3


def s():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS player_master (player_id INTEGER PRIMARY KEY AUTOINCREMENT, player_name text)")

    user_input = input("Your name? > ")
    make_player = f"INSERT INTO player_master(player_name) VALUES ('{user_input}')"
    cur.execute(make_player)

    for player_id, player_name in cur.execute("SELECT * FROM player_master"):
        print(player_id, player_name)
    player_id = 1
    cur.execute(
        "CREATE TABLE IF NOT EXISTS player_status (player_id int, money int)")
    make_status = f"INSERT INTO player_status VALUES ({player_id}, 0)"
    cur.execute(make_status)
    for row in cur.execute("SELECT * FROM player_status"):
        print(row)
    print("OK")

s()