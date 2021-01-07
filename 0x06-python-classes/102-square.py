#!\usr\bin\python3
"""compare two areas"""


class Square:
    """define class to square"""

    def __init__(self, size=0):
        """instantition of size"""
        self._size = size

    @property
    def size(self):
        """get size attribute"""
        return self._size

    @size.setter
    def size(self, value):
        if type(self._size) is not int:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """define the area of a Square"""
        return self._size ** 2

    def __eq__(self, other):
        """Compare if square is equal to another by area"""
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area"""
        return self.size != other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area """
        return self.size > other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area"""
        return self.size >= other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area"""
        return self.size <= other.size

    def __lt__(self, other):
        """Compare if square is less than another by area"""
        return self.size < other.size
