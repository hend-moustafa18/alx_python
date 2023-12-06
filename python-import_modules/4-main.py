#!/usr/bin/python3
if __name__ == "__main__":
        raise_exception = __import__('4-raise_exception').raise_exception
try:
    raise_exception()
except TypeError as te:
    print("Exception has been raised")