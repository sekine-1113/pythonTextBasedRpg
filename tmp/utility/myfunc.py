import json


def read_json(fp: str) -> dict:
    with open(fp, "r", encoding="UTF-8") as f:
        return json.load(f)


def yes_or_no(text: str="") -> None:
    yes = ("yes", "y")
    no = ("no", "n")
    user_input = input(text).lower()
    if user_input in yes:
        print("Yes")
    elif user_input in no:
        print("No")
    else:
        print("Yes or No")
