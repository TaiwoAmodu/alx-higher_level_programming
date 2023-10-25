#!/usr/bin/python3
class Square:
    """Represent a square."""

    def __init__(self, side=0):
        """Initialize a new Square.

        Args:
            side (int): The length of each side of the square.
        """
        self.side = side

    @property
    def side(self):
        """Get/set the side length of the square."""
        return self.__side

    @side.setter
    def side(self, value):
        if not isinstance(value, int):
            raise TypeError("Side length must be an integer")
        if value < 0:
            raise ValueError("Side length must be >= 0")
        self.__side = value
