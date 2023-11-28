#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
# YOUR CODE HERE
if lastdigit > 5:
    print("Last digit of", number, "is", lastdigit, "and is greater than 5") 
if lastdigit == 0:
    print("Last digit of", number, "is", lastdigit, "and is 0") 
if lastdigit < 6:
    print("Last digit of", number, "is", lastdigit, "and is less than 6 and not 0") 
