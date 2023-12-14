"""Define inherits_from Function"""
def inherits_from(obj, a_class):
    """Check The Object is an instance of a class
    that inherited (directly or indirectly) 
    from the specified class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False