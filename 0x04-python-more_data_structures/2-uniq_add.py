#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    summ = 0
    for i in my_list:
        t = 0
        for el in new_list:
            if el == i:
                t += 1
        if t == 0:
            new_list.append(i)
            summ += i
    return summ
