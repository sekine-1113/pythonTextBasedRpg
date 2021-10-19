from version1.system.character import *

def print_profile():
    print( "____________________")
    print( "|==================|")
    print( "|** Your Profile **|")
    print( "|==================|")
    print(f"|LEVEL   : {PLAYER_LEVEL:8}|")
    print(f"|HITPOINT: {PLAYER_HITPOINT:8}|")
    print(f"|POWER   : {PLAYER_POWER:8}|")
    print( "￣￣￣￣￣￣￣￣￣￣")

PLAYER_NAME = "Alice"
ENEMY_NAME = "Slime"

print(f"Welcome to TextBasedRpg, {PLAYER_NAME}!")
print_profile()
