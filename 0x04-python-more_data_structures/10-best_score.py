#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        s = 0
        r = ""
        for i in a_dictionary:
            if a_dictionary[i] > s:
                s = a_dictionary[i]
                r = i
        return r
    else:
        return None
