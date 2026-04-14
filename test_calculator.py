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
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5.0)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(2, -1)
    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
if __name__ == "__main__":
    unittest.main()
