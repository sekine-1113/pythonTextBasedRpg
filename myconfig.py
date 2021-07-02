import sys
import os
from pprint import pprint


user = {
    "name": "Player",
    "Job1" : {
        "Name": "Job1",
        "JpnName" : "ジョブ1",
        "MaxLv": 50,
        "Lv" : 1
    },
    "Job2" : {
        "Name": "Job2",
        "JpnName" : "ジョブ2",
        "MaxLv": 50,
        "Lv" : 1
    },
    "Job3" : {
        "Name": "Job3",
        "JpnName" : "ジョブ3",
        "MaxLv": 50,
        "Lv" : 1
    },
    "status": {
        "Limit": {
            "Lv": 100
        }
    },
    "Inventory" : {
        "Item" : {
            "Heal1": {
                    "count":0
                }
        },
        "Equip" : {},
        "TMP" : {}
    },
    "SHINKOU" : {
        "QUEST" : {
            "1-1" : False,
            "1-2" : False
        }
    },
    "money" : 0,
}

system = {
    "auto_save": False,
    "root": os.path.dirname(sys.argv[0])
}


if __name__ == "__main__":
    pprint(user)