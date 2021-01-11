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
        if self._width == 0 or self._height == 0:
            return 0
        return (self._height + self._width) * 2

    def __print__(self):
        """print #"""
        if self._width == 0 or self._height == 0:
            return 0
        for i in range(self._height):
            for j in range(self._weidth):
                print('#')

    def __str__(self):
        """print #"""
        a = ''
        if self._width == 0 or self._height == 0:
            return 0
        a = (('#' * self._width) + '\n') * (self._height - 1)
        a = a + ('#' * self.width)
        return a
