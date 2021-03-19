'''
ip_address.py

    -This prints local IP, Public IP, and Hostname to stdout
'''

import socket
from requests import get

# get hostname
host = socket.gethostname()

# get local ip
local_ip = socket.gethostbyname(host)

# get public ip
public_ip = get('https://api.ipify.org').text

# log output
print(f'Local IP: {local_ip}')
print(f'Public IP: {public_ip}')
print(f'Hostname: {host}')
