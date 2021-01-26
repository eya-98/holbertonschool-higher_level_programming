#!/usr/bin/python3
"""Holberton Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """define a subclass class Square"""
    def __init__(self, size):
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)
    
    def __str__(self):
        """print square details"""
        return "[Square] {}/{}".format(self.__size, self.__size)
