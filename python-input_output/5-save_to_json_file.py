#!/usr/bin/python3
"""Defines JSON representation function"""
import json


def save_to_json_file(my_obj, filename):
    """Returns represented JSON object to file"""

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
