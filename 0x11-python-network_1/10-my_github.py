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
    req = requests.get('https://api.github.com/user', auth=(username, passwd))
    try:
        print(r.json()['id'])
    except Exception:
        print('None')