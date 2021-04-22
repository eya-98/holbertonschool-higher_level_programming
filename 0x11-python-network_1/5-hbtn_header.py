#!/usr/bin/python3
"""
sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    print(request.headers.get('X-Request-Id'))
