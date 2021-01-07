#!/usr/bin/python3
"""square module"""


class Square:
    """creating a class to the square"""
    
    def __init__(self, size=0, position=(0, 0)):
        """instantiation of size and position"""
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """get of size"""
        return self._size
        
    @size.setter
    def size(self, value):
        """set the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value
    
    @property
    def position(self):
        """get the position"""
        return self._position
    
    @position.setter
    def position(self, value):
        """set value to Position"""
        if type(value) is not tuple or type(value[0]) is not int \
           or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[0] < 0 or value [1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self._position = value
    
    def area(self):
        """return the area of the square"""
        return self._size * self._size
    
    def my_square(self, value):
        """print # or empty line"""
        a = ""
        if self.size == 0:
            a = ""
            return a
        if self.position[1] < 0:
            a = "\n"
        a = a + (" " * self.position[0] + "#" * self.size + "\n") * self.size
        return a

    def my_print(self):
        """print # and spaces"""
        if self._size == 0:
            print("")
        else:
            for i in range(self._position[1]):
                print("")
            for n in range(self._size):
                for j in range(self._position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print("")
