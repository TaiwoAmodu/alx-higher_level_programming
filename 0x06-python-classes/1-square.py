#!/usr/bin/python3
"""Defines a Square class."""

class Square:
    """Represent a square."""

    class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The length of each side of the square.
        """
        self.__size = size

# Instantiate a Square with size 3
my_square = Square(3)

# Check the object's type
print(type(my_square))

# Access the private attribute via name mangling
print(my_square.__dict__)

# Try to access the private attribute (this will raise an error)
try:
    print(my_square.__size)
except AttributeError as e:
    print(e)
