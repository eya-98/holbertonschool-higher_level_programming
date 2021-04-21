#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    """POST REQUEST"""
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    mail = urllib.parse.urlencode(value).encode('utf-8')
    requests = urllib.request.Request(url, mail)
    with urllib.request.urlopen(requests) as response:
        print (response.read().decode('UTF-8'))
