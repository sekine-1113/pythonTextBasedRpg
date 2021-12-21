from random import randint
import sys, os
from games.aq7.funcs import call
from games.aq7.gui import details

def game1(coin):
    text = "ルール\n"
    text += "倍率は1~100倍の任意の倍数を選べます\n"
    text += "掛け金はカジノコイン10~1000枚の任意の枚数を選べます\n"
    text += "ベットは掛け金ｘ倍率です\n"
    text += "勝った場合はベットが2倍^勝利数になります\n"
    text += "負けた場合はベットが0になり終了します\n"
    text += "引き分けの場合は勝利数が1増えますがベットの増減はありません\n"
    text += "配当は最大1024倍です"
    details("ルール",text)
    o = call(min_count=1,d_count=100+1,txt="倍率を入力してください")
    p = call(min_count=10*o,d_count=1000*o+1,txt=f"掛け金を{10*o}~{1000*o}の間で入力してください")
    coin -= p
    base, win, get_coin = 50, 0, 0
    while True:

        if win == 10: return coin
        r = randint(1,100)
        a = call(2,f"{base}より上か下か 1:上 0:下")
        if base < r and a == 1 or r < base and a == 0:
            print("結果:",r)
            print("あなたの勝ちです")
            win += 1
            p *= 2
            get_coin += p
            print(f"{p}コイン獲得!")
            cnt = call(2,"続けますか? 1:はい 0:いいえ ")
            if cnt == 1: base = r
            elif cnt == 0: return coin + get_coin
        elif r == base:
            print("結果:",r)
            print("引き分けです")
            win += 1
        else:
            print("結果:",r)
            print("あなたの負けです")
            print("終わります")
            p = 0
            return coin
    coin += get_coin
    return coin

