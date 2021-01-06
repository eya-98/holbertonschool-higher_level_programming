#!/usr/bin/python3
"""class defines square"""


class Square:
    """square"""
    def __init__(self, size=0, position=(0, 0)):
        """private instance attribute"""
        self._size = size
        self._position = position

    @property
    def size(self):
        """define size as a property"""
        return self._size

    @property
    def position(self):
        """define position as a property"""
        return self._position

    @size.setter
    def position(self, value):
        """sit the value of position"""
        if value is not tuple or value[0] >= 0 and value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    @size.setter
    def size(self, value):
        """sit the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """returns the square"""
        a = self._size * self._size
        return a

    def my_print(self):
        """print # and spaces"""
        if self._size == 0:
            print("")
            return
        for i in range(self._position[1]):
            print("")
        for i in range(self._size):
            for j in range(self._position[0]):
                print(" ", end="")
            for k in range(self.size):
                print("#", end="")
            print("")
