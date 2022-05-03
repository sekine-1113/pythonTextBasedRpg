import json
import requests
import os
import sys
from pathlib import Path


# config_dir contains a sompleRPG settings file
config_dir = Path("./config")
# temp_dir contains a running simpleRPG backup file
temp_dir = Path("./temp")
# save_dir contains a simpleRPG savefile
save_dir = Path("./save")


__simpleRPG_config = "https://raw.githubusercontent.com/alice-1113/pythonTextBasedRpg/main/config.json"
__simpleRPG_config_localdir = config_dir
__simpleRPG_config_localfile = "config.json"
__simpleRPG_config_localpath = __simpleRPG_config_localdir / __simpleRPG_config_localfile

print(__simpleRPG_config_localpath)


if not config_dir.exists():
    config = {}

try:
    config = requests.get(__simpleRPG_config).json()
except requests.ConnectionError as e:
    print(e.response)
    config = {
        "game_config": {
            "using_lang": "ja",
            "allow_lang": [
                "ja",
                "en"
            ]
        },
        "using_dirs": {
            "base": ""
        },
        "game_version": "0.0.0"
    }

base_dir = Path(sys.argv[0]).parent
config["using_dirs"]["base"] = str(base_dir)

def change_lang(config, new_lang="ja"):
    if new_lang in config["game_config"]["allow_lang"]:
        config["game_config"]["using_lang"] = new_lang
        return config
    raise Exception
def get_available_lang(config):
    return config["game_config"]["allow_lang"]
def get_using_lang(config):
    return config["game_config"]["using_lang"]
def check_game_version(config):
    return config["game_version"] == "1.0.0"

def read_text():
    text_json = base_dir.parent / "text.json"
    with open(text_json, "r", encoding="UTF-8") as fp:
        return json.load(fp)

def display_text(text_key):
    global config
    messages = read_text()
    using_lang = get_using_lang(config)
    text = messages[using_lang][text_key]
    print(text)

for lang in get_available_lang(config):
    change_lang(config, lang)
    if not check_game_version(config):
        print("lang:", lang)
        display_text("update")