#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and 
uses the GitHub API to display your id
"""
from sys import argv
import requests


if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    req = requests.get('' , auth=(username, passwd))
    if req.status_code > 200:
        print('None')
    else:
         print(r.json()['id'])