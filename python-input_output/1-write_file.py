#!/usr/bin/python3
"""
This module contains a functain
"""


def write_file(filename="", text=""):
    """
    Write a text file and prints it.


    Args:
    filename(str): The name of the file to write

    Returns:
    None
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

