from pathlib import Path

# config_dir contains a sompleRPG settings file
config_dir = Path("./config")
# temp_dir contains a running simpleRPG backup file
temp_dir = Path("./temp")
# save_dir contains a simpleRPG savefile
save_dir = Path("./save")


if not config_dir.exists():
    print("not config_dir.exists()")

