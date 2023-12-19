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