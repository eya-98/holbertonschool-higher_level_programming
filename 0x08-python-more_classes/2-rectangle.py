#!/usr/bin/python3
"""define module to define Rectangle"""


class Rectangle:
    """define Rectangle class"""

    def __init__(self, width=0, height=0):
        """instantiation of width and height)"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """retrieve width"""
        return self._width

    @width.setter
    def width(self, value):
        """set width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """retrieve width"""
        return self._height

    @height.setter
    def height(self, value):
        """set width value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """define area"""
        return self._width * self._height

    def perimeter(self):
        """define the perimeter"""
        if width == 0 or height == 0:
            return 0
        return (self._height + self._width) * 2
