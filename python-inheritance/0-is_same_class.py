"""Define is same class Function"""
def is_same_class(obj, a_class):
    """Check The Object is Exactly an instance of the Specified Class """
    if type(obj) == a_class:
        return True
    return False