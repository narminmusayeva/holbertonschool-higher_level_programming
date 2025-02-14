#!/usr/bin/python3
def read_file(filename, "r"):
"""
Reads a text file (UTF8) and prints its content to stdout.

Args:
    filename (str): The name of the file to read. Defaults to an empty string.

Returns:
    None
"""


    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end = "")
