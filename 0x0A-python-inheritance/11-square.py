#!/usr/bin/python3
""" Holberton Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from rectangle class"""
    def __init__(self, size):
        """Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Square size"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
