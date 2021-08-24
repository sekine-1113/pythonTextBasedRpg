import random


DRAW, PLAYER_WIN, PLAYER_LOSE = range(3)  # 0, 1, 2

hand = {
    1: "グー",
    2: "チョキ",
    3: "パー"
}

hand_win = [
    [DRAW, PLAYER_WIN, PLAYER_LOSE],
    [PLAYER_LOSE, DRAW, PLAYER_WIN],
    [PLAYER_WIN, PLAYER_LOSE, DRAW]
]

ai_hand = random.randint(1, 3)

player_hand = 0
while not 0 < player_hand < 4:
    player_hand = int(input())

print(hand[player_hand], hand[ai_hand])

win = hand_win[player_hand-1][ai_hand-1] == PLAYER_WIN
lose = hand_win[player_hand-1][ai_hand-1] == PLAYER_LOSE

msg = "PLAYER WIN" if win is True \
    else "PLAYER LOSE" if lose is True \
    else "DRAW"

print(msg)  # OK