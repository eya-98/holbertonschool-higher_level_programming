#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    ch = ''
    for i in str:
        if i != str[n]:
            ch += i
    return ch
