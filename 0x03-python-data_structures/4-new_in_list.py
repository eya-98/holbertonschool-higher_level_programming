#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        c = my_list
        return c
    elif idx >= len(my_list):
        c = my_list
        return c
    else:
            c = my_list[:]
            c[idx] = element
            return (c)
