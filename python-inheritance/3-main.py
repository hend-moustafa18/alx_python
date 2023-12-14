#!/usr/bin/python3
if __name__== "__main__":
 BaseGeometry = __import__('3-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))