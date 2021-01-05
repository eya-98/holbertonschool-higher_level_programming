#!/usr/bin/python3
"""class defines square"""


class Square:
    """square"""
    def __init__(self, size=0):
        """private instance attribute"""
        try:
            self.__size = size
            if size < 0:
                raise Exception
        except TypeError:
            print("size must be an integer")
        except (ValueError, Exception):
            print("size must be >= 0")
