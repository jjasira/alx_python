
"""
    In this module we will learn about class declarations
"""
class Square:
    """
    This is the class declaration
    """
    def __init__(self, size=0):
        """
        this is a private instance variable
        """
        self.__size = size
        
    @property
    def size(self):
        return self.__size
        """This method gets the size of the square"""
    
    @size.setter
    def size(self, value):
        
        self.__size = value
        """This methos sets the size of the square"""

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        
        """raise a type error exception"""
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        """raise a value error exception"""

    def area(self):
        return self.__size ** 2
        """This method calculates the area of the square"""

    def my_print(self):
        """Printing the square in std form"""
        if self.__size > 0:
            for i in range(self.__size+1):
                for j in range(self.__size+1):
                    print("#")
        else:
            print(" ")