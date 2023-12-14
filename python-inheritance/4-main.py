#!/usr/bin/python3
if __name__== "__main__":
 BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
    