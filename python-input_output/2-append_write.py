#!/usr/bin/python3
"""
This module contains is a function
"""
def append_write(filename="", text=""):
    """
    Append a text filne and print it

    Args:
    filename(str): The name of file to append

    Returns:
    None
    """
    open with(filename, "a", encoding="utf-8") as f:
        return f.append(text)
