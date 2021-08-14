import json


def read_json(fp):
    with open(fp, "r", encoding="UTF-8") as f:
        return json.load(f)