import json


def read_json(fp: str) -> dict:
    with open(fp, "r", encoding="UTF-8") as f:
        return json.load(f)


def yes_or_no(text: str="") -> bool|None:
    yes = ("yes", "y")
    no = ("no", "n")
    user_input = input(text).lower()
    if user_input in yes:
        return True
    elif user_input in no:
        return False
    else:
        return
