#!/user.bin.python3
def no_c(my_string):
    j = 0
    str = ""
    for i in my_string:
        if i != "c" and i != "C":
            str = str + i
    return str
