#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter method to set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
    
    

       
