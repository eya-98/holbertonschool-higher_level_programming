#!/usr/bin/python3
"""

Holberton test module

"""


def print_square(size):
    """

    prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print("")
