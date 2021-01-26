#!/usr/bin/python3
""" Holberton Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from rectangle class"""
    def __init__(self, size):
        """define size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """print details about the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
