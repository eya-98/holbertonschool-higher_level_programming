#!/usr/bin/python3
"""Holberton Module"""


def read_file(filename=""):
    """define a function that read file"""
    with open(filename, mode="r", encoding="UTF-8") as filee:
        print(filee.read())
