#!/usr/bin/python3
"""
This script demonstrates the usage of the Square class.

It creates an instance of the Square class, initializes it with a size, and showcases accessing attributes.

Usage:
- Import the Square class from the '0-square' module.
- Create an instance of Square with a specified size.
- Print the type of the instance and its attributes.
- Attempt to access the 'size' and '__size' attributes, catching and printing any exceptions.
"""
if __name__ == "__main__": 
  Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
