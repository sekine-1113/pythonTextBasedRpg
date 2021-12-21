from games.aq7.funcs import call
import sys, os, time
from math import log10
from random import randint,choice,choices

def level_up(player_data,jobID):
    rise = [
        {'MaxHP':7,'MaxMP':4,'ATK':5,'DF':7,'Wis':3},
        {'MaxHP':6,'MaxMP':7,'ATK':3,'DF':4,'Wis':8},
        {'MaxHP':5,'MaxMP':8,'ATK':2,'DF':3,'Wis':9},
        {'MaxHP':6,'MaxMP':3,'ATK':6,'DF':5,'Wis':3},
        {'MaxHP':6,'MaxMP':5,'ATK':4,'DF':5,'Wis':3},
        {'MaxHP':6,'MaxMP':6,'ATK':4,'DF':5,'Wis':6},
        {'MaxHP':5,'MaxMP':2,'ATK':8,'DF':3,'Wis':2},
        {'MaxHP':7,'MaxMP':9,'ATK':4,'DF':5,'Wis':9},
        {'MaxHP':8,'MaxMP':7,'ATK':7,'DF':6,'Wis':6}
    ]
    keys = rise[jobID].keys()
    for i in keys:
        player_data[i] += randint(int(rise[jobID][i]/1.1),rise[jobID][i])
    return player_data

def skills_data(f,ID,JobID,LV,r=False):
    """f = f_deal(attack.csv).fread()..."""
    s = [f[i] for i in range(len(f)) if f[i]["ID"]==ID and f[i]["Lv"]<=LV and f[i]["JobID"]==JobID]
    if r == True: return s
    if 0 == len(s): return True
    print("ID スキル 消費MP")
    for i, v in enumerate(s): print(i,v["Name"],v["MP"])
    d = call(len(s),"")
    if d <= i: return s[d]

def skill(base,equip,edf,mgn):
    fond = (base+equip)/2 - edf/4
    _ = int(fond/16)
    if _ < 0: _ = 0
    fond += randint(-_,_) + randint(-1,1)
    fond = int(fond *float(mgn))
    if fond < 0: fond = randint(0,1)
    return int(fond)

def spell(base,equip,mgn):
    fond = (base+equip) * float(mgn)
    _ = int(fond/32)
    fond += randint(-_,_) + randint(-1,1)
    return int(fond)

def battle_func(skl,user,equip,job,monster):
    acs = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==4000][user["Acs"]]
    equip = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==3000][user["Equip"]]
    jobid = user["JobID"]
    jobdata = job[jobid]
    enemies = []
    for i in range(len(monster)):
        if jobdata["Lv"]-5 <= monster[i]["Lv"] <= jobdata["Lv"]+5:
            enemies.append(monster[i])
        elif monster[i]["ID"] == 0:  # メタル系
            enemies.append(monster[i])
    enemy, drop = choice(enemies), choices([0,1,2],[4,3*(1+acs["NDROP"]),1*(1+acs["RDROP"])])[0]
    print(f"{enemy['Name']}があらわれた!")
    while 0 < jobdata["HP"]:
        print(f"{user['UserName']}はどうする?")
        f = call(5,"1:こうげき 2:じゅもん 3:とくぎ 4:ステータス 0:にげる\n")
        attack, count = 0, 0
        if f == 1:
            attack = skill(jobdata["ATK"],equip["ATK"]+acs["ATK"],enemy["DF"],1)
            if choices([0,1],[7,1])[0] == 1:
                print("かいしんのいちげき!")
                attack = attack * 3 + randint(1,6)
            if 0 < attack:
                print(f"{enemy['Name']}に{attack}のダメージをあたえた!")
            else: print("ダメージをあたえられなかった!")
        elif f == 2:
            sdata = skills_data(skl,1000,jobid,jobdata["Lv"])
            if sdata == True:
                print("じゅもんをおぼえていない!")
                continue
            if sdata["type"] == 0:
                for i in range(sdata["Count"]):
                    _ = spell(jobdata["Wis"],equip["Wis"]+acs["Wis"],sdata["Mgn"])
                    if choices([0,1],[7,1])[0] == 1:
                        print("じゅもんがぼうそうした!")
                        _ *= 3
                    if "メタル" in enemy['Name']:
                        _ = 0
                    if 0 < _:
                        print(f"{enemy['Name']}に{_}のダメージをあたえた!")
                    else: print("ダメージをあたえられなかった!")
                    attack += _
                    count += 1
                if 1 < count: print(f"{enemy['Name']}に合計{attack}のダメージをあたえた!")
            elif sdata["type"] == 1:
                _ = spell(jobdata["Wis"],equip["Wis"]+acs["Wis"],sdata["Mgn"])
                if jobdata["HP"] + _ <= jobdata["MaxHP"]:
                    jobdata["HP"] += _
                else: jobdata["HP"] = jobdata["MaxHP"]
                print(f"HPが{_}回復した!")
        elif f == 3:
            sdata = skills_data(skl,2000,jobid,jobdata["Lv"])
            if sdata == True:
                print("とくぎをおぼえていない!")
                continue
            print(f"{user['UserName']}の{sdata['Name']}!")
            if sdata['Name'] == "ぬすむ":
                if randint(0,2) == 0:
                    drop = choices([0,1,2],[0,6*(1+acs["NDROP"]),4*(1+acs["RDROP"])])[0]
                    print(f"{user['UserName']}はなにかをぬすんだ!")
                else:
                    print(f"{user['UserName']}はなにもぬすめなかった!")
            else:
                for i in range(sdata["Count"]):
                    _ = skill(jobdata["ATK"],equip["ATK"]+acs["ATK"],enemy["DF"],sdata["Mgn"])
                    if choices([0,1],[7,1])[0] == 1:
                        print("かいしんのいちげき!")
                        _ = _ * 3 + randint(1,6)
                    if 0 < _:
                        print(f"{enemy['Name']}に{_}のダメージをあたえた!")
                    else: print("ダメージをあたえられなかった!")
                    attack += _
                    count += 1
                if 1 < count: print(f"{enemy['Name']}に合計{attack}のダメージをあたえた!")
        elif f == 4:
            print("職業:",jobdata["Name"],"/ Lv:",jobdata["Lv"])
            print("HP:",jobdata["HP"],"/",jobdata["MaxHP"])
            print("MP:",jobdata["MP"],"/",jobdata["MaxMP"])
            continue
        elif f == 0:
            drop = None
            return skl, user, job, drop
        enemy["HP"] -= attack
        time.sleep(0.5)
        if enemy["HP"] <= 0:
            print(f"{enemy['Name']}をたおした!")
            if drop == 1: drop = enemy["NDROP"]
            elif drop == 2: drop = enemy["RDROP"]
            else: drop = None
            if not(drop is None): print(f"{enemy['Name']}は{drop}をおとしていった!")
            enemy["EXP"] = int(enemy["EXP"]*(1+int(equip["EXP"])+int(acs["EXP"])))
            print(f"{user['UserName']}は{enemy['EXP']}経験値を手に入れた!")
            print(f"{enemy['GOLD']*(1+equip['GOLD']+acs['GOLD'])}Gかくとく!")
            user["GOLD"] += enemy['GOLD']*(1+equip["GOLD"]+acs['GOLD'])
            next_exp = int(jobdata["Lv"] ** log10(jobdata["Lv"])*6 + jobdata["Lv"]*15)
            old = jobdata["Lv"]
            while enemy["EXP"] >= next_exp:
                enemy["EXP"] -= next_exp
                jobdata["EXP"] += next_exp
                jobdata = level_up(jobdata,jobid)
                jobdata["Lv"] += 1
                next_exp = int(jobdata["Lv"] ** log10(jobdata["Lv"])*6 + jobdata["Lv"]*15)
            else:
                if old != jobdata["Lv"]:
                    print(f"レベルが{old}から{jobdata['Lv']}にあがった!")
                next_exp -= enemy["EXP"]
                jobdata["EXP"] += enemy["EXP"]
            return skl, user, job, drop
        if enemy["ID"] == 0:
            if choices([0,1],[3,1])[0] == 1:
                print(f"{enemy['Name']}はにげだした!")
                break
        enemy_attack = skill(enemy["ATK"],0,jobdata["DF"],1) + 1
        jobdata["HP"] -= enemy_attack
        print(f"{enemy['Name']}のこうげき!")
        print(f"{user['UserName']}は{enemy_attack}のダメージをうけた!")
        if jobdata["HP"] <= 0:
            print(f"{user['UserName']}はたおされてしまった")
            jobdata["HP"] = 1
            if 1 < user["GOLD"]:
                user["GOLD"] -= int(user["GOLD"]/2)
                print(f"{user['UserName']}は{int(user['GOLD']/2)}G失った")
                drop = None
            return skl, user, job, drop
    return skl, user, job, drop
