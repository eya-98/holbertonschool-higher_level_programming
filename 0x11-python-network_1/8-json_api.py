#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user 
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = argv[1]
    else:
        q = ""
    res = requests.post(url, {'q': q})

    try:
        request = res.requests.json()
        if request:
            print("[{}] {}".format(request.get('id'), request.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')