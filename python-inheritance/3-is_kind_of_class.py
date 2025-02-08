#!/usr/bin/python3
"""
defines a class-checking function
"""


def is_kind_of_class(obj, a_class):
    """check if an object is excatly an instance of given class"""
    return isinstance(obj, a_class)
