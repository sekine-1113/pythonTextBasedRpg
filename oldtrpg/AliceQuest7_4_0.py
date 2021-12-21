import sys, os, time
from random import randint, choices

from games.aq7.fio import f_deal
from games.aq7.funcs import call
from games.aq7.battle import battle_func, skills_data
from games.aq7.items import consume, get_item
from games.aq7.gui import details
from games.aq7.facility import shop_func, shop_func2
from games.aq7.facility import darma,rest,casino


def main():
    f = f_deal(dir_path=os.path.dirname(sys.argv[0])).is_dir()
    f_c = f + r"/datas"
    base_skl = f_deal(f_c + r"/attack.csv")
    base_user = f_deal(f_c + r"/user.csv")
    base_job = f_deal(f_c + r"/job.csv")
    base_equip = f_deal(f_c + r"/equips.csv")
    base_item = f_deal(f_c + r"/items.csv")
    skl = base_skl.fread()
    user = base_user.fread()[0]
    job = base_job.fread()
    equip = base_equip.fread()
    item = base_item.fread()
    jobid = user['JobID']
    acs = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==4000]
    eqi = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==3000]
    e_acs, e_eqi = acs[user["Acs"]], eqi[user["Equip"]]
    while True:
        title = call(4,"1:ぼうけんのしょ 2:せってい 3:セーブ 0:おわる ")
        if title == 1:
            print(f"なまえ: {user['UserName']} 職業:{job[jobid]['Name']} Lv:{job[jobid]['Lv']}")
            if user['UserName'] == "------":
                name_change = call(2,"ここで名前を変更していきますか? 1:はい 0:いいえ ")
                if name_change == 1:
                    while True:
                        user['UserName'] = input("6文字までで新しい名前を入力してください >> ")[0:6]
                        check = call(2,f"{user['UserName']}でよろしいですか? 1:はい 0:いいえ ")
                        if check == 1: break
                elif name_change == 0: pass
        elif title == 2:
            text = f"using directrys:\n{f}\n{f_c}\n"
            if user["AUTO"] == 0:
                user["AUTO"] = False
            else: user["AUTO"] = True
            text += f"オートセーブ: {user['AUTO']}\n"
            text += f"ゲーム内の名前: {user['UserName']}"
            details("せってい",text)
            if call(2,"Open top-level directory? 1:Yes 0:No\n"):
                os.system(f"explorer {f}")
            if call(2,"オートセーブを有効にしますか? 1:はい 0:いいえ "):
                user["AUTO"] = 1
            else: user["AUTO"] = 0
            continue
        elif title == 3:
            print("data saved",base_user.fwrite(header=user.keys(),values=user))
            print("data saved",base_job.fwrite(header=job[0].keys(),values=job))
            print("data saved",base_equip.fwrite(header=equip[0].keys(),values=equip))
            print("data saved",base_item.fwrite(header=item[0].keys(),values=item))
        elif title == 0: break
        do = 0
        while True:
            if user["AUTO"] == 1:
                base_user.fwrite(header=user.keys(),values=user)
                base_job.fwrite(header=job[0].keys(),values=job)
                base_equip.fwrite(header=equip[0].keys(),values=equip)
                base_item.fwrite(header=item[0].keys(),values=item)
            hoge = call(6,"1:すすむ 2:アイテム 3:そうび 4:ステータス 0:タイトルへ")
            if hoge == 1:
                do += 1
                if do % 4 == 0:
                    print("宿屋についた!")
                    user, job = rest(user, job)
                elif do % 7 == 0:
                    print("武器屋についた!")
                    buys = call(3,"1:買いにきた 2:売りにきた 0:やめる ")
                    if buys == 1:
                        eqi, user['GOLD'] = shop_func(eqi,user['GOLD'])
                    elif buys == 2:
                        eqi, user['GOLD'] = shop_func2(eqi,user['GOLD'])
                    elif buys == 0: pass
                elif do % 9 == 0:
                    print("アクセサリー屋についた!")
                    buys = call(3,"1:買いにきた 2:売りにきた 0:やめる ")
                    if buys == 1:
                        acs, user['GOLD'] = shop_func(acs,user['GOLD'])
                    elif buys == 2:
                        acs, user['GOLD'] = shop_func2(acs,user['GOLD'])
                    elif buys == 0: pass
                elif do % 5 == 0:
                    print("ダーマ神殿についた!")
                    cjob = call(2,"1:転職する 0:やめる ")
                    if cjob == 1:
                        user, job = darma(user, job)
                        jobid = user["JobID"]
                    elif cjob == 0: pass
                elif do % 11 == 0:
                    print("カジノについた!")
                    cdo = call(3,"1:遊ぶ 2:景品交換 0:やめる ")
                    if cdo == 1: user = casino(user)
                    elif cdo == 2:
                        acs, user["COIN"] = shop_func(acs,user["COIN"])
                    elif cdo == 0: pass
                else:
                    monster = f_deal(f_c+r"/monster.csv").fread()
                    skl, user, job, drop = battle_func(skl,user,equip,job,monster)
                    if not(drop is None): item = get_item(item,drop)
            elif hoge == 2:
                item, user, job, eqi = consume(item,user,job,eqi)
            elif hoge == 3:
                print("ぶき:",e_eqi["Name"])
                print("アクセサリー:",e_acs["Name"])
                equip_change = call(2,"装備を変えますか? 1:はい 0:いいえ ")
                if equip_change == 1:
                    new_eqi = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==3000 and equip[i]["STOCK"]]
                    print("武器")
                    for i, e in enumerate(new_eqi):
                        print(i, e["Name"],"ATK:",e["ATK"],"WIS:",e["Wis"])
                    new_ind = call(len(new_eqi),"")
                    user["Equip"] = new_eqi[new_ind]['EquipID']
                    if new_eqi[new_ind]["Name"] == "なし": pass
                    else: print(f"{eqi[user['Equip']]['Name']}を装備しました")
                    e_eqi = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==3000][user["Equip"]]
                    new_acs = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==4000 and equip[i]["STOCK"]]
                    print("アクセサリー")
                    for i, e in enumerate(new_acs): print(i, e["Name"])
                    new_ind = call(len(new_acs),"")
                    user["Acs"] = new_acs[new_ind]['EquipID']
                    if new_acs[new_ind]["Name"] == "なし": pass
                    else: print(f"{acs[user['Acs']]['Name']}を装備しました")
                    e_acs = [equip[i] for i in range(len(equip)) if equip[i]["ID"]==4000][user["Acs"]]
            elif hoge == 4:
                text = f"名前: {user['UserName']}\n"
                text += f"ゴールド: {user['GOLD']} G\n"
                text += f"カジノコイン: {user['COIN']} 枚\n"
                text += f"職業: {job[jobid]['Name']}\n"
                text += f"Lv: {job[jobid]['Lv']} / {job[jobid]['MaxLv']}\n"
                text += f"HP: {job[jobid]['HP']} / {job[jobid]['MaxHP']}\n"
                text += f"MP: {job[jobid]['MP']} / {job[jobid]['MaxMP']}\n"
                text += f"ATK: {job[jobid]['ATK']} + {e_eqi['ATK']+e_acs['ATK']}\n"
                text += f"DF: {job[jobid]['DF']}\n"
                text += f"WIS: {job[jobid]['Wis']} + {e_eqi['Wis']+e_acs['ATK']}\n"
                text += f"E: {e_eqi['Name']}\n"
                text += f"E: {e_acs['Name']}\n"
                text += "じゅもん:\n"
                for i in skills_data(skl,1000,jobid,job[jobid]['Lv'],True):
                    text += f"{i['Name']}\n"
                text += "とくぎ:\n"
                for i in skills_data(skl,2000,jobid,job[jobid]['Lv'],True):
                    text += f"{i['Name']}\n"
                details("ステータス",text)
            elif hoge == 0: break

for i in range(4):
    sys.stdout.write(f"loading{'.'*i}\r")
    time.sleep(0.2)

main()