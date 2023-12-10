"""we define a function that checks if an object inherits from a class"""
def inherits_from(obj, a_class):
    """we will use the type and isinstance methods"""
    return issubclass(type(obj), a_class) and type(obj) != a_class