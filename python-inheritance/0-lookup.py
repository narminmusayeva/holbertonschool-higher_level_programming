#!/usr/bin/python3
"""
    0-lookup module
    Search available attributes and methods of an object
"""
def lookup(obj):
    """
    This function returns the list of available attributes
    and methods of an object.
    """
    return dir(obj)

