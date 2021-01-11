#!/usr/bin/python3
"""define module to define Rectangle"""


class Rectangle:
    """define Rectangle class"""

    def __init__(self, width=0, height=0):
        """instantiation of width and height)"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve width"""
        return self.__height

    @height.setter
    def height(self, value):
        """set width value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """define area"""
        return self.__width * self.__height

    def perimeter(self):
        """define the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """print #"""
        a = ''
        if self.__width == 0 or self.__height == 0:
            return a
        a = (('#' * self.__width) + '\n') * (self.__height - 1)
        a += '#' * self.__width
        return a
