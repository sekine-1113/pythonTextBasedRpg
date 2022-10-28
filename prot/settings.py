import sys
import os


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
    pass
