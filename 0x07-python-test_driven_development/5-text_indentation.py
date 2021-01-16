#!/usr/bin/python3
"""


Holberton module

"""


def text_indentation(text):
    """prints a text with 2 new lines after 
    each of these characters: ., ? ;"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        new = text
        new = new.replace('.', '.\n\n')
        new = new.replace(':', ':\n\n')
        new = new.replace('?', '?\n\n')
        print(new.strip())
