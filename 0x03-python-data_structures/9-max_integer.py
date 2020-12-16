#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        num = my_list[0]
        for i in my_list:
            if i > num:
                num = i
        return num
