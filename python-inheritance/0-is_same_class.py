"""This function checks if an object is an instance of a class"""
def is_same_class(obj, a_class):
    """We will check this using the inbuilt isinstance() method"""
    if isinstance(obj, a_class):
        return True
    else:
        return False