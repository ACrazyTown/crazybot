import logging
import datetime
import os

def main_logger():
    date_format_file = "%d%m%Y_%H%M%S"
    date_format = "%d/%m/%Y %H:%M:%S"

    logfile = f"logs/log_{datetime.datetime.now().strftime(date_format_file)}.txt"
    if not os.path.exists(logfile):
        with open(logfile, "w") as f:
            f.write("="*15 + "[ BEGIN LOG ]" + "="*15 + "\n") 
    else:
        pass  

    logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(), logging.FileHandler(logfile)], format="[%(asctime)s | %(module)s - %(funcName)s | %(name)s | %(levelname)s] %(message)s", datefmt=date_format)