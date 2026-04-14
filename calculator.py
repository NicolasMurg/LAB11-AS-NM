import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except ValueError as e:
        raise ValueError(e)

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a
def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)
def exponent(a, b):
    return a ** b

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(sub(8, 3), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(log(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 8)

if __name__ == "__main__":
    unittest.main()
