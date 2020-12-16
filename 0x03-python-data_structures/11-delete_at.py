#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        list = []
        for i in range(len(my_list)):
            if i != idx:
                list.append(my_list[i])
        my_list = list
        return my_list
