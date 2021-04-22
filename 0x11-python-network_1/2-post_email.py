#!/usr/bin/python3
"""sends a POST request"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    mail = urllib.parse.urlencode(value).encode('utf-8')
    requests = urllib.request.Request(url, mail)
    with urllib.request.urlopen(requests) as response:
        print(response.read().decode('UTF-8'))
