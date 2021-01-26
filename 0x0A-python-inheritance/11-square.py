#!/usr/bin/python3
""" square """
Rectangle = __import__("10-square").Square


class Square(Rectangle):
    """ class square """
    def __str__(self, size):
        return ("[Square] {}/{}".format(size, size))
