#!/usr/bin/python3
"""Defines a Square class."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The length of each side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size length must be an integer")
        if value < 0:
            raise ValueError("Size length must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def perimeter(self):
        """Return the perimeter of the square."""
        return 4 * self.__size
