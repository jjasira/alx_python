"""we define our base class"""
class BaseGeometry():
    """This is our base class"""
    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """"in this method we will raise an exception"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        


"""This class will inherit from the base class"""
class Rectangle(BaseGeometry):
    """This class will inherit from the base class but with more functionality"""
    def __init__(self, width, height):
        """we will initialize the following fields and validate them"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """this method calculates the area"""
        return self.__width * self.__height
    
    def __str__(self) -> str:
        """return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def print(self):
        """print the rectangle"""
        print(str(self))
    



class Square(Rectangle):
    """This class inherits from the Rectangle class."""
    def __init__(self, size):
        """We define a field for the size and validate it"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """we define an area method that overides the superclass"""
        return self.__size ** 2