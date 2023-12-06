#!/usr/bin/python3
if __name__ == "__main__":
    raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg
try:
    message = "C is fun"
    raise_exception_msg(message)
except NameError as ne:
    print(ne)
