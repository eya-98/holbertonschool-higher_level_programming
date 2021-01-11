#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """define rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instantation"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """define height"""
        return self.__height

    @property
    def width(self):
        """define width"""
        return self.__width

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def _print(self):
        """print rectangle"""
        if self.__width == 0 or self.__height == 0:
            print('')
        else:
            for i in range(0, height):
                for j in range(0, width):
                    print('#', end="")
                if i < self.__height - 1:
                    print('')

    def __str__(self):
        """print rectangle"""
        ch = ''
        if self.__width == 0 or self.__height == 0:
            ch = ''
            return ch
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    ch = ch + Rectangle.print_symbol
                if i < self.__height - 1:
                    ch = ch + '\n'
        return ch

    def __repr__(self):
        """return a string representation of the rectangle to recreate"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """delete an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
