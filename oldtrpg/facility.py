from games.aq7.funcs import call
from games.aq7.games.high_low import game1

def bshop(data):
    print("番号 名前 ATK WIS G/COIN")
    for i, item in enumerate(data):
        if i == 0: continue
        if "ふくびき券" in item["Name"]: continue
        print(i,item['Name'],item['ATK'],item['Wis'],item['Price'])

def shop_func(data,gold):
    bshop(data)
    buy = call(len(data),"どれを買いますか? 0:やめる ")
    if buy == 0: return data, gold
    else:
        if data[buy]['Price'] <= gold:
            _ = gold
            gold -= data[buy]['Price']
            print(data[buy]['Name'],"を買いました")
            print(f"{_}G/COIN → {gold}G/COIN")
            data[buy]['STOCK'] += 1
        else:
            print("お金が足りなかった!")
        return data, gold

def shop_func2(data,gold):
    bshop(data)
    buy = call(len(data),"どれを売りますか? 0:やめる ")
    if buy == 0: return data, gold
    else:
        _ = gold
        gold += int(data[buy]['Price']/10)
        print(data[buy]['Name'],"を売りました")
        print(f"{_}G → {gold}G")
        data[buy]['STOCK'] -= 1
    return data, gold

def darma(user,job):
    if 75 <= job[0]["Lv"] and 75 <= job[3]["Lv"]:
        job[6]["Can"] = 1
    if 75 <= job[1]["Lv"] and 75 <= job[2]["Lv"]:
        job[7]["Can"] = 1
    if 90 <= job[6]["Lv"] and 90 <= job[7]["Lv"]:
        job[8]["Can"] = 1
    print("どの職業に転職しますか?\nID 職業 Lv")
    for i in range(len(job)):
        if job[i]["Can"] == 1:
            print(i,job[i]["Name"],job[i]["Lv"])
    while True:
        jobid = call(i+1,"9:やめる")
        if jobid == 9: return user, job
        check = call(2,f"{job[jobid]['Name']}に転職しますか?1:はい 0:いいえ ")
        if check == 1: user["JobID"] = jobid
        elif check == 0: continue
        return user, job

def rest(user,job):
    jobid = user["JobID"]
    gold = user["GOLD"]
    price = job[jobid]["Lv"] * 8
    r = call(2,f"{price}Gで宿屋に泊まりますか? 1:はい 0:いいえ ")
    if r == 1:
        if 0 <= gold - price:
            gold -= price
            print("宿屋に泊まった!")
            print("HPとMPが全回復した!")
            job[jobid]["HP"] = job[jobid]["MaxHP"]
            job[jobid]["MP"] = job[jobid]["MaxMP"]
        else: print("ゴールドが足りなかった!")
    return user, job

def casino(user):
    coin = user["COIN"]
    gold = user["GOLD"]
    max_change = gold//10
    print("10Gでカジノコイン1枚と交換できます")
    change = call(2,"交換しますか? 1:はい 0:いいえ")
    if change == 1:
        print(f"最大{max_change}枚交換できます")
        coin += call(max_change+1,f"交換枚数 1~{max_change} 枚")
        gold -= max_change * 10
        print(f"カジノコインが{coin}枚になりました")
    if coin < 10:
        print("コインが足りません")
        return user
    else:
        play = call(2,"ハイアンドローゲームをプレイする? 1:はい 0:いいえ ")
        if play == 1: coin = game1(coin)
        else: pass
    return user
