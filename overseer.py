import os
import sys
import json
import subprocess

client_os = os.name
verbose = True
up = "[UPDATER]"
repo = "https://github.com/ACrazyTown/crazyBot"

def update():
    if verbose != False:
        print(f"[INIT-UPDATER] Verbose is set to {verbose}, running in Verbose mode...")
        print(f"{up} Attempting to update...")
        print(f"{up} Attempting to update using main repository... ({repo})")
        if client_os != "posix":
            print("Windows is not supported... yet")
        try:
            print(f"{up} Stashing local repository...")
            os.system("git stash")
            print(f"{up} Reset local repository to default settings!") 
            print(f"{up} Attempting to pull crazyBot repo using Git...")
            os.system(f"git pull {repo}")
            print(f"{up} Pulled crazyBot repo successfully!")
            os.system("git stash pop")
        except:
            print(f"{up} Uh oh! Something went wrong.")
        print(f"{up} Finished!")
    else:
        print(f"{up} Attempting to update...")
        if client_os != "posix":
            print("Windows is not supported... yet")
        try:
            os.system("git stash")
            os.system(f"git pull {repo}")
            print(f"{up} Pulled repo successfully!")
            os.system("git stash pop")
        except:
            print(f"{up} Uh oh! Something went wrong.")
        print(f"{up} Finished!")

def start_bot():
    while True:
        print("$ - Starting bot...")
        bot = subprocess.Popen([sys.executable, "bot.py", "overseer=True"])
        bot.wait()

        print(f"[BOT] Returned code {bot.returncode}")

        if bot.returncode == 1:
            print("[BOT] Rebooting...")
            main()

        elif bot.returncode == 2:
            print("[BOT] Rebooting without updating...")
            start_bot()

        elif bot.returncode == 3:
            print("[BOT] Shutting down...")  
            break  

def main():
    print("=== BEGIN OVERSEER ===")
    print("-- Updating --")
    update()
    print("-- Starting bot --")
    start_bot()

if __name__ == "__main__":
    main()
