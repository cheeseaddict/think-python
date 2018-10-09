import math


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result


print(distance(1,2,4,6))

"""
As an exercise, use incremental development to write a function called hypotenuse that
returns the length of the hypotenuse of a right triangle given the lengths of the other two
legs as arguments. Record each stage of the development process as you go.
"""

def hypotenuse(a, b):
    # a**2 + b**2 = c**2
    # square_a = a**2
    # square_b = b**2
    # c = square_a + square_b
    # result = math.sqrt(c)
    return math.sqrt(a**2 + b**2)


print(hypotenuse(3, 4)) # => 5.0
