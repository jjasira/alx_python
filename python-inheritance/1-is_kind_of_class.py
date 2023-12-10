"""we define a function that compares if an object is an instance of a class"""
def is_kind_of_class(obj, a_class):
    """we use the type and isinstance methods"""
    return isinstance(obj, a_class) or type(obj) == a_class