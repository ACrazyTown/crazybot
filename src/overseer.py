import os
import sys
import json
import subprocess
import time
import shutil
import glob
import logging
from crazylogger import main_logger

try:
    os.chdir(__file__.replace(os.path.basename(__file__), ""))
except:
    pass

client_os = os.name
verbose = True
clean_logs_on_start = True
check_for_git_enabled = True
op = "[OVERSEER]"
up = "[UPDATER]"
bp = "[BOT]"
repo = "https://github.com/ACrazyTown/crazyBot"

if clean_logs_on_start == True:
    files = glob.glob("logs/*.txt")
    print(files)
    for f in files:
        os.remove(f)
    print("Erased all logs.")

def clean_json_temp():
    with open("data.json", "r") as f:
        data = json.load(f)

    data["crazybot"]["temp"]["on_reboot"] = "False"
    data["crazybot"]["temp"]["channel_id"] = ""

    with open("data.json", "w") as f:
        json.dump(data, f)

def check_for_git():
    if check_for_git_enabled == True: 
        loggerMain.info(f"Running 'check_git()'")
        loggerMain.debug(f"You can turn this setting of by specifying 'check_for_git' to be 'False'.")
        loggerMain.info(f"Checking if Git is installed...")
        gitlocate = shutil.which("git")
        if gitlocate != None:
            loggerMain.info("Git is installed.")
        else:
            loggerMain.critical("Git is not installed! Try installing Git and trying again!")
            exit()
    else:
        pass

def update():
    if verbose != False:
        loggerMain.debug(f"[INIT-UPDATER] Verbose is set to {verbose}, running in Verbose mode...")
        print(f"{op} Checking if Git is installed...")
        check_for_git()
        print(f"{up} Attempting to update using main repository... ({repo})")
        try:
            print(f"{up} Resetting local repository...")
            os.system("git reset --hard")
            print(f"{up} Reset local repository to default settings!")
            print(f"{up} Attempting to pull crazyBot repo using Git...")
            os.system(f"git pull {repo}")
            print(f"{up} Pulled crazyBot repo successfully!")
            os.system("git stash pop")
            print(f"{up} Restored data.json")
        except:
            print(f"{up} Uh oh! Something went wrong.")
        print(f"{up} Finished!")
    else:
        print(f"{up} Attempting to update...")
        try:
            os.system("git reset --hard")
            os.system(f"git pull {repo}")
            print(f"{up} Pulled repo successfully!")
            os.system("git stash pop")
        except:
            print(f"{up} Uh oh! Something went wrong.")
        print(f"{up} Finished!")

def start_bot():
    while True:
        print(f"{bp} Starting...")
        bot = subprocess.Popen(["node", "bot.js"])
        bot.wait()

        print(f"{bp} Returned code {bot.returncode}")

        if bot.returncode == 1:
            print(f"{bp} Shutting down...")
            break

        elif bot.returncode == 2:
            print(f"{bp} Rebooting without updating...")
            start_bot()

        elif bot.returncode == 3:
            print(f"{bp} Rebooting...")  
            main()

def main():
    global loggerMain, loggerUpd, loggerBot
    loggerMain = logging.getLogger("Overseer Main Logger")
    loggerUpd = logging.getLogger("Overseer Updater Logger")
    loggerBot = logging.getLogger("Overseer Bot Logger")
    main_logger()

    print("=== BEGIN OVERSEER ===")
    print(f"{op} Updating...")
    check_for_git()
    update()
    print(f"{op} Starting Bot...")
    start_bot()

if __name__ == "__main__":
    main()
