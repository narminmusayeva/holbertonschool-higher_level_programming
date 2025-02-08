#!/usr/bin/python3
"""
contains in MyList class
"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""


    def print_sorted(self):
        """Print a list in sorted acsending order"""
        print (sorted(self))
