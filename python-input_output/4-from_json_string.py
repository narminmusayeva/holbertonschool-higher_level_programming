#!/usr/bin/python3
"""Defines JSON representation function"""
import json


def from_json_string(my_str):
    """Returns the JSON represented by JSON string"""

    return json.loads(my_str)
