#!/usr/bin/python3
"""Defines JSON representation function"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation
    """

    return json.dumps(my_obj)
