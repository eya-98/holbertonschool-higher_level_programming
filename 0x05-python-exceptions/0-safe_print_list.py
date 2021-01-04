#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    k = 0
    for k in range(0, x):
            try:
                print("{}".format(my_list[k]), end="")
                j += 1
            except:
                pass
    print("")
    return j
