#!/usr/bin/python3
"""HOLBERTON MODULE"""


class MyList(list):
    """Mylist inherits attributes and methods from list"""
    def __init__(self):
        """initiation of all the attributes"""
        super().__init__()

    def print_sorted(self):
        """print the list, but sorted"""
        print(sorted(self))
    
