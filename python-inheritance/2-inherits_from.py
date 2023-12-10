"""we define a function that checks if an object inherits from a class"""
def inherits_from(obj, a_class):
    return isinstance(obj, a_class) or type(obj) == a_class