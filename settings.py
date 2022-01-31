import sys
import os

from ctypes import windll, wintypes, byref



class Input:
    def __init__(self) -> None:
        super().__init__()

    def integer(self, prompt:str="> ") -> int:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            return self.integer(prompt)

    def integer_with_range(self, prompt:str="> ", _min:int=0, _max:int=0) -> int:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if _min <= user_input <= _max:
                return user_input
            return self.integer_with_range(prompt, _min, _max)
        except ValueError:
            return self.integer_with_range(prompt, _min, _max)



def exsits(path) -> bool:
    return os.path.exists(path)


def mkdirs(dirs_path) -> bool:
    if not os.path.exists(dirs_path):
        os.makedirs(dirs_path)
    return os.path.exists(dirs_path)


DIR = os.path.abspath(os.path.dirname(sys.argv[0]))

DATABASE_DIR_NAME = "data"
DATABASE_DIR_PATH = os.path.abspath(
    os.path.join(DIR, DATABASE_DIR_NAME))

DATABASE_FILE_NAME = "test.db"
DATABASE_FILE_PATH = os.path.abspath(
    os.path.join(DATABASE_DIR_PATH, DATABASE_FILE_NAME))

MASTER_DATA = [
    "rank_master",
    "class_master",
    "abilities_master",
    "quests_master",
    "enemies_master"
]
MASTER_DATA_FILE_EXTENSION = "csv"
MASTER_DATA_PATHES = [
    file_name + "." + MASTER_DATA_FILE_EXTENSION
    for file_name in MASTER_DATA
]

CONFIG_FILE_NAME = "config.json"
CONFIG_FILE_PATH = os.path.abspath(
    os.path.join(DIR, CONFIG_FILE_NAME))



if __name__ == "__main__":
    input_ = Input()
    input_.integer_with_range(_max=3)
