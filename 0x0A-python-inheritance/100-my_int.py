#!/usr/bin/python3
"""Holberton Module"""


class MyInt(int):
    """define Myint class"""
    def __eq__(self, other):
        """define elquality"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """define elquality"""
        return not super().__ne__(other)
