#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for k in my_list:
        print("{}".format(k), end="")
        j += 1
        x -= 1
        if x == 0:
            break
    return j
