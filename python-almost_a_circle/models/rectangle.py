"""In this module we will explore python classes further"""
class Base:
    """This is a private class attribut"""
    __nb_objects = 0
    def __init__(self, id=None):
        """We will test if the id property is not None then we will assign it"""
        if id != None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


"""This is out Rectangle class that will inherit from our base class"""
class Rectangle(Base):
    """this is the class contructor for our Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """we call the superclass constructor"""
        super().__init__(id)
        
        """Assign each argument to the right attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Getter and setter for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_positive(value, "width")
        self.__width = value

    """getter and setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_positive(value, 'height')
        self.__height = value

    """getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_non_negative(value, "x")
        self.__x = value

    """getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_non_negative(value, "y")
        self.__y = value

    """validation methods"""
    def validate_positive(self, value, attribute_name):
        """Validation method for positive integers"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")
    
    def validate_non_negative(self, value, attribute_name):
        """Validation method for x and y"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
        
    def area(self):
        """we will calculate the area by multiplying the height and the width"""
        return self.height * self.width