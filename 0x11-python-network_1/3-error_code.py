#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import sys
import urllib.request
from urllib.error import HTTPError, URLError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
