#!/usr/bin/python3
if __name__ == "__main__": # define the class
  Square = __import__('0-square').Square
# define the class
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
# define the class
try:
    print(my_square.size)
except Exception as e:
    print(e)
# define the class
try:
    print(my_square.__size)
except Exception as e:
    print(e)
