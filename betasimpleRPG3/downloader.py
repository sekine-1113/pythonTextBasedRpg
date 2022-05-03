import requests

URL = "https://raw.githubusercontent.com/alice-1113/pythonTextBasedRpg/main/betasimpleRPG2/data/players.json"
res = requests.get(URL).json()

print(res)
