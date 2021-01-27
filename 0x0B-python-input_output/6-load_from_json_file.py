#!/usr/bin/python3
"""Holberton Module"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, "r", encoding="UTF-8") as filee:
        return json.load(filee)
