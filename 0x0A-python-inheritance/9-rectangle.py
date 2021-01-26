#!/usr/bin/python3
"""Holberton Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""

    def __init__(self, width, height):
        """instantiation of width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """raise an exception"""
        return self.__height * self.__width

    def __str__(self):
        """print rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
