import configparser
import os

config = configparser.ConfigParser()
config.read(r"version5\config.ini")

cmd = r"python version4\argparser.py"
playerId = config.get("runOptions", "playerId")
developMode = config.get("runOptions", "developMode")
if int(developMode):
    logLevel = config.get("logLevel", config.get("runOptions", "logLevel"))
    cmd = f"{cmd} --playerId={playerId} --develop {logLevel}"
else:
    cmd = f"{cmd} --playerId={playerId}"
print(cmd)
os.system(cmd)