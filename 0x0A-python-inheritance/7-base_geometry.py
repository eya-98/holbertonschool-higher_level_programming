#!/usr/bin/python3
"""class base geometry base on the previous class"""


class BaseGeometry():
    """class base geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    """check positive num"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
