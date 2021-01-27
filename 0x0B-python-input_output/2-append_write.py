#!/usr/bin/python3
"""Holberton Module"""


def append_write(filename="", text=""):
    """append text to a file"""
    with open(filename, "a+", encoding="UTF-8") as filee:
        filee.write(text)
        return len(text)
