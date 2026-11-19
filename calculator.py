"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try: return math.sqrt(a)
    except ValueError: raise ValueError("cannot take the square root of a negative number")

def hypotenuse(a, b):
    try: return math.hypot(a, b)
    except TypeError: raise TypeError("hypotenuse requires numeric inputs")
    
# First example
def add(a, b): return a + b
def subtract(a, b): return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("The divisor must be nonzero.")
    return b / a

def logarithm(a, b): 
    if a <= 0 or a == 1:
        raise ValueError("base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b