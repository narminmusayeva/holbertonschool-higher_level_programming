#!/usr/bin/python3
"""This module defines a square class that calculates the area of a square."""

class Square:
    """Represents a square with private size attribute"""

    def __init__(self, size=0):
        """Initializes a new square instance.

        Args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
