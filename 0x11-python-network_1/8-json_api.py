#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user 
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = sys.argv[1]
    except Exception:
        lq = ''
    res = post(url, data={'q': q})

    try:
        request = res.json()
        if request:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')