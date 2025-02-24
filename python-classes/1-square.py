#!/usr/bin/python3

"""This module defines a Square class."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
