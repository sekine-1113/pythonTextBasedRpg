from games.aq7.funcs import call
from games.aq7.gui import details

def consume(item,user,jobs,eqi=None):
    job = jobs[user['JobID']]
    haves = [i for i in item if 0 < i['STOCK']]
    haves.insert(0,0)
    text = "ID 名前\t個数\t効果\n"
    for index, i in enumerate(haves):
        if index == 0: continue
        text += f"{index} {i['Name']} {i['STOCK']}\t{i['com']}\n"
        print(index, i['Name'])
    details("アイテム",text)
    itemid = call(len(haves),"どれを使いますか? 0:何も使わない ")
    if itemid == 0: return item, user, jobs, eqi
    count = 1
    if 1 < haves[itemid]['STOCK']:
        count = call(haves[itemid]['STOCK']+1,f"何個使いますか?1~{haves[itemid]['STOCK']}まで")
    for _ in range(count):
        print(haves[itemid]["Name"],"を使った!")
        if 0 < haves[itemid]["HP"]:
            if 0 < job['HP'] < job['MaxHP']:
                if job['HP'] + haves[itemid]['HP'] <= job['MaxHP']:
                    job['HP'] += haves[itemid]['HP']
                    print(f"HPが{haves[itemid]['HP']}回復した!")
                elif job['MaxHP'] < job['HP'] + haves[itemid]['HP']:
                    job['HP'] = job['MaxHP']
                    print(f"HPが{job['HP']}になった!")
                haves[itemid]['STOCK'] -= 1
            else: print("効果がなかった!")
        elif 0 < haves[itemid]["MP"]:
            if 0 < job['MP'] < job['MaxMP']:
                if job['MP'] + haves[itemid]['MP'] <= job['MaxMP']:
                    job['MP'] += haves[itemid]['MP']
                    print(f"MPが{haves[itemid]['MP']}回復した!")
                elif job['MaxMP'] < job['MP'] + haves[itemid]['MP']:
                    job['MP'] = job['MaxMP']
                    print(f"MPが{job['MP']}になった!")
                haves[itemid]['STOCK'] -= 1
            else: print("効果がなかった!")
        elif "引換券" in haves[itemid]["Name"]:
            eqi = get_item(eqi,haves[itemid]["Name"].replace("引換券",""))
    return item, user, jobs, eqi

def get_item(item,drop=None):
    haves = [i for i in item]
    for i in haves:
        if i['Name'] == drop:
            i['STOCK'] += 1
        else: continue
    return item