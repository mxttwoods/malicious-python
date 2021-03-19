""" 
wifi_extractor.py 

    - This script will extract a array of wifi credentials from a windows PC
"""

import subprocess
from typing import List

# pull data from the subproc
data: List[str] = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)

# clean up data
extracted_creds: List[str] = [
    line.split(":")[1][1:-1] for line in data if "All User Profile" in line
]

# for each in ...
for creds in extracted_creds:
    # pull data from subproc
    results = (
        subprocess.check_output(["netsh", "wlan", "show", "profiles"])
        .decode("utf-8")
        .split("\n")
    )

    # clean up data
    results = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]

    # try plz
    try:
        # log creds
        print(f"SSID: {creds}, Pass: {results[0]}")
        # 'x': open for exclusive creation, failing if the file already exists
        new_file = open("wifi_creds.txt", "x")
        # 'w': open for writing, truncating the file first
        new_file = open("wifi_creds.txt", "w")
        # write to file
        new_file.write(f"SSID: {creds}, Pass: {results[0]}")
        # close file
        new_file.close()
    # badboy
    except SystemError:
        # log if error
        print(f"SSID: {creds}, Pass: Not Found")
        # raise error
        raise
