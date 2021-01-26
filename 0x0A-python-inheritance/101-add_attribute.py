#!/usr/bin/python3
"""Holberton Module"""


def add_attribute(obj, attribute, value):
    """add attribute to an object"""

    if hasattr(obj, '__dict__'):
        obj.__setattr__(attribute, value)
    else:
        raise TypeError("can't add new attribute")
