#!/usr/bin/python3
"""create a module"""


class _MagicClass__radius:
    """create a class"""
    from math import pi
    
    def __init__(self, radius=0):
        """initiation of radius"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.radius = radius

    def area(self):
        """define the area of a circle"""
        return pi * (self.radius ** 2)
        
    def circumference(self):
        """define the circumference"""
        return pi * 2 * self.radius
