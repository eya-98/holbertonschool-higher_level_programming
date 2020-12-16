#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    s = []
    for j in range(len(my_list)):
        if my_list[j] % 2 != 0:
            s.append(False)
        else:
            s.append(True)
    return s
