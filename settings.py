import sys
import os

from ctypes import windll, wintypes, byref


class Singleton:
    def __new__(cls, *args, **kwargs) -> "Singleton":
        if not hasattr(Singleton, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Input(Singleton):

    @classmethod
    def integer(self, prompt:str="> ") -> int:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            return self.integer(prompt)

    @classmethod
    def integer_with_range(self, prompt:str="> ", _min:int=0, _max:int=0) -> int:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if _min <= user_input <= _max:
                return user_input
            return self.integer_with_range(prompt, _min, _max)
        except ValueError:
            return self.integer_with_range(prompt, _min, _max)


def unlock_ansi():
    # ANSIエスケープシーケンス解除
    STD_OUTPUT_HANDLE = -11
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

    kernel32 = windll.kernel32
    hOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    dwMode = wintypes.DWORD()
    kernel32.GetConsoleMode(hOut, byref(dwMode))
    dwMode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32.SetConsoleMode(hOut, dwMode)


class Color:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLO = "\033[33m"
    BLUE = "\033[34m"
    MAZENTA = "\033[35m"
    CIAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    N = "\033[38;5;{}m"


class BackGroundColor:
    BLACK = "\033[40m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    YELLO = "\033[43m"
    BLUE = "\033[44m"
    MAZENTA = "\033[45m"
    CIAN = "\033[46m"
    WHITE = "\033[47m"
    RESET = "\033[0m"
    N = "\033[48;5;{}m"



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
