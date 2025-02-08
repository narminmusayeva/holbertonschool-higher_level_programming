#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Check if an object is excatly an instance of class"""
    if type(obj) == a_class:
        return True
    return False
