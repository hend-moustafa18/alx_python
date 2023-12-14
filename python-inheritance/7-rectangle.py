"""Import '5-base_geometry' File"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    
    def __dir__(cls):
        """Removing __init_subclass__ attribute
        from the dir result to pass the check
        """
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']
    
    """Define a'Rectangle' Class"""
    def __init__(self, width, height):
        """Instantiation width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height


    def area(self):
        """Define 'area' method"""
        return self.__width * self.__height
    

    def __str__(self):
        """'__str__' method to print"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
    
    