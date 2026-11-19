import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, -6), -10)
        self.assertEqual(add(0, 7), 7)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(3, 8), -5)
        self.assertEqual(subtract(4, -2), 6)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(4, 2), 0.5)
        self.assertAlmostEqual(div(3, 1), 1 / 3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1), 0)
        self.assertAlmostEqual(logarithm(4, 2), 0.5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 8)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(1, 1), 2 ** 0.5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.41421356)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
