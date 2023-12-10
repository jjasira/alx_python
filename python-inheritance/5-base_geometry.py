"""we define our base class"""
class BaseGeometry():
    """This is our base class"""
    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """"in this method we will raise an exception"""
        if type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than zero".format(name))