from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """we call the superclass constructor"""
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """override the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.validate_positive(value, "size")
        self.width = value
        self.height = value