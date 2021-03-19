''' 
subdomain_scanner.py 

    - This script will scan a domain name for a set of subdomian names
'''
import requests
from io import TextIOWrapper
from typing import List

# the domain to scan for subdomains
domain = "google.com"

# read all subdomains
file: TextIOWrapper = open("subdomains.txt")

# read all content
content: str = file.read()

# split by new lines
subdomains: List[str] = content.splitlines()

# a list of discovered subdomains
discovered_subdomains = []

# for each in ...
for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        print("[+] Discovered subdomain:", url)
        # append the discovered subdomain to our list
        discovered_subdomains.append(url)

# save the discovered subdomains into a file
with open("discovered_subdomains.txt", "w") as f:
    # write each result
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)
