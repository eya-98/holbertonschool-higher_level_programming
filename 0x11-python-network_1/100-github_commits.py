#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos" + owner + "/" + repo + "/commits"
    reqs = requests.get(url)
    requets = reqs.json()[:10]
    for req in requets:
        sha = req['sha']
        commits = req['commit']['author']['name']
        print("{}: {}".format(sha, commits))
