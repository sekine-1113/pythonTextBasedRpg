# ============================================================================
# demo Simple Text Based RPG.
# ============================================================================

# ============================================================================
# import libraries
# ============================================================================

# ============================================================================
# functions
def create_player_status():
    return {
        "max_level": 20,
        "level": 1,
        "max_hp": 30,
        "hp": 30,
        "strength": 12,
        "exp": 0
    }

def create_enemy_status():
    return {
        "max_hp": 20,
        "hp": 20,
        "strength": 8,
        "exp": 4
    }

def check_status(player):
    print("="*40)
    print("Name:", player["name"])
    for k, v in player["status"].items():
        print(f"{k}: {v}")
    print("="*40)
# ============================================================================

# ============================================================================
# global variables
mainloop = True
battleloop = False
command = None
battle_command = None
player = {
    "status": create_player_status()
}
enemy = {
    "name": "Slime",
    "status": create_enemy_status()
}
# ============================================================================

# ============================================================================
# constant variables
DEBUG = True
PROMPT = ">> "
# ============================================================================

# ============================================================================
# start game
print("Hi, Please tell me your name.")
if DEBUG: player["name"] = "Alice"
else: player["name"] = input(PROMPT)
print("Hello,", player["name"])
# ============================================================================

# ============================================================================
# main game

while mainloop:
    print("What do you do?")
    print("1:Explore 2:Status 0:Exit")
    command = input(PROMPT)
    if command == "0":
        mainloop = False
    elif command == "1":
        print(f"{enemy['name']} appeared!")
        battleloop = True
        while battleloop:
            print(f"What will {player['name']} do?")
            print("1:Attack 2:Escape")
            battle_command = input(PROMPT)
            if battle_command == "1":
                print(f"{player['name']}'s attack!")
                print(f"{player['status']['strength']} damage to {enemy['name']}!")
                enemy["status"]["hp"] -= player["status"]["strength"]
                if enemy["status"]["hp"] <= 0:
                    print(f"Defeated {enemy['name']}!")
                    print(f"Earn {enemy['status']['exp']} exp")
                    player["status"]["exp"] += enemy["status"]["exp"]
                    if player["status"]["max_level"] > player["status"]["level"] and player["status"]["exp"] % 8 == 0:
                        player["status"]["level"] += 1
                        player["status"]["max_hp"] += 2
                        player["status"]["hp"] = player["status"]["max_hp"]
                        player["status"]["strength"] += 3
                        print("Level up!")
                        print(f"Level: {player['status']['level']-1} -> {player['status']['level']}")
                    battleloop = False
                else:
                    print(f"{enemy['name']}'s attack!")
                    print(f"{player['name']} received {enemy['status']['strength']} damage!")
                    player["status"]["hp"] -= enemy["status"]["strength"]
                    if player["status"]["hp"] <= 0:
                        print(f"{player['name']} fell down!")
                        battleloop = False
            elif battle_command == "2":
                print("Run away!")
                battleloop = False
    elif command == "2":
        check_status(player)
    else:
        continue
# ============================================================================

# ============================================================================
# end game
print("Thank you for playing. See you.")
if not DEBUG:
    input()
# ============================================================================