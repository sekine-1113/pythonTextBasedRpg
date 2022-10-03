
import json
from pathlib import Path
import sys


parentPath = Path(sys.argv[0]).parent
saveDir = parentPath / "save"
backupDir = parentPath / ".backup"
configFile = parentPath / "config.json"
config = {
    "path": {
        "parentPath": str(parentPath),
        "saveDir": str(saveDir),
        "backupDir": str(backupDir)
    },
    "game": {
        "lang": "jp",
        "allowLang": ["jp", "en"]
    },
    "gameText": {
        "jp": {
            "battleStart": "バトル開始!"
        },
        "en": {
            "battleStart": "Start Battle!"
        }
    }
}

if False:
    if configFile.exists():
        with configFile.open("r", encoding="UTF-8") as f:
            config = json.load(f)
    else:
        with configFile.open("w", encoding="UTF-8") as f:
            json.dump(config, f, indent=4)

gameConfig = config.get("game")
lang = gameConfig.get("lang")
lang = "en"
gameText = config.get("gameText")

print(gameText.get(lang).get("battleStart"))