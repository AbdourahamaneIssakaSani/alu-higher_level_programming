#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Creates a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize data."""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += '#'
            rectangle += '\n'
        return rectangle[:-1]

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of width, must be >=0
        """
        if not isinstance(value, int):
            print(isinstance(value, int))
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        Args:
            value: value of height, must be >=0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
