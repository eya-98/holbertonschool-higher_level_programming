#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        for i in range(len(my_list)):
            c = my_list
            if i == idx:
                c[i] = element
    return c
