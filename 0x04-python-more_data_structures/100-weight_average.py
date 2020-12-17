#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        summ = 0
        j = 0
        for i in range(len(my_list)):
            summ += my_list[i][0] * my_list[i][1]
            j += my_list[i][1]
        return summ / j
