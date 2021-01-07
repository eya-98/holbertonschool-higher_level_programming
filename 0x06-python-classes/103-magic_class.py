#!/usr/bin/python3
"""create a module"""
from math import pi


class MagicClass:
    """create a class"""

    def __init__(self, radius=0):
        """initiation of radius"""
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._radius = radius

    def area(self):
        """define the area of a circle"""
        return pi * (self._radius ** 2)

    def circumference(self):
        """define the circumference"""
        return pi * 2 * self._radius
