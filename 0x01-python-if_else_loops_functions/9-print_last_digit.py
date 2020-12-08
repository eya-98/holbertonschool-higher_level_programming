#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if n < 0:
        n = n * -1
    last = n % 10
    print("{:d}".format(last), end="")
    return last
