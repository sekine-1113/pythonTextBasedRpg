
from main import Fighter, Sage, Wizard


print("TextBasedRPG")
print("[1] Start [0] Quit")
user_input = int(input(">> "))

if not user_input:
    exit("Bye.")


player_data = {
    "name": "Alice",
    "level": 1,
    "money": 0,
    "item": [],
    "role": 0
}

player_name = input("What your name? >> ")

if player_name:
    player_data['name'] = player_name


print(f"Hello, {player_data['name']}!")

roles = {
    1: Fighter,
    2: Wizard,
    3: Sage
}

while True:
    print("is your role?")

    print("[1] Fighter [2] Wizard [3] Sage")
    user_input = int(input(">> "))

    if roles.get(user_input):
        player = roles.get(user_input)(player_data["level"])
        break


player.show()
