#!/usr/bin/python
"""Holberton Module"""


def write_file(filename="", text=""):
    """write some text in the file"""
    with open(filename, "w", encoding="UTF-8") as filee:
        filee.write(text)
    return len(text)
