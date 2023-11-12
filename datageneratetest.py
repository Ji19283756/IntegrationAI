import unittest
from datagenerate import *
from math import *

class TestSum(unittest.TestCase):

    def test_trapezoid_sum_poly0(self):
        func = MathFunction("x", lambda x: x)

        # tests the function x
        self.assertEqual(func.trap_reimann(0, 1, 1), 0.5, f"Should be 0.5")
        self.assertEqual(func.trap_reimann(0, 1, 2), 0.5, f"Should be 0.5")
        self.assertEqual(func.trap_reimann(0, 1, 4), 0.5, f"Should be 0.5")

        # works in the reverse
        self.assertEqual(func.trap_reimann(1, 0, 1), -0.5, f"Should be -0.5")
        self.assertEqual(func.trap_reimann(1, 0, 2), -0.5, f"Should be -0.5")
        self.assertEqual(func.trap_reimann(1, 0, 4), -0.5, f"Should be -0.5")

    def test_trapezoid_sum_poly1(self):
        func = MathFunction("x(-x+4)", lambda x: x * (-x + 4))

        # tests the function x(-x + 4)
        self.assertEqual(func.trap_reimann(0, 4, 1), 0, f"Should be 0")
        self.assertEqual(func.trap_reimann(0, 4, 2), 8, f"Should be 8")
        self.assertEqual(func.trap_reimann(0, 4, 4), 10, f"Should be 10")

        # works in reverse
        self.assertEqual(func.trap_reimann(4, 0, 1), 0, f"Should be 0")
        self.assertEqual(func.trap_reimann(4, 0, 2), -8, f"Should be -8")
        self.assertEqual(func.trap_reimann(4, 0, 4), -10, f"Should be -10")

    def test_trapezoid_sum_poly_exp(self):
        func = MathFunction("x * e ^ x + 1", lambda x: x * pow(e, x) + 1)

        # tests the function x(e^x)+1
        self.assertEqual(round(func.trap_reimann(0, 4, 1), 7), 440.7852003, f"Should be 440.7852003")
        self.assertEqual(round(func.trap_reimann(0, 4, 2), 7), 251.9488245, f"Should be 251.9488245")
        self.assertEqual(round(func.trap_reimann(0, 4, 4), 7), 190.9493049, f"Should be 190.9493049")

    def test_trapezoid_sum_poly2(self):
        func = MathFunction("sqrt((x^2 + 3x)/2) - (4x - 7)/3 * 5",
                            lambda x: sqrt((pow(x, 2) + 3 * x) / 2) - (4 * x - 7) / 3 * 5)

        self.assertEqual(round(func.trap_reimann(0, 16, 1), 7), -568.0360426, f"Should be -568.0360426")
        self.assertEqual(round(func.trap_reimann(0, 16, 2), 7), -564.285358, f"Should be -510.1676322")

    def test_trapezoid_sum_trig(self):
        func = MathFunction("sin(22x)+cos(-x)+tan(x/2)+e^x",
                            lambda x: sin(22 * x) + cos(-x) + tan(x / 2) + pow(e, x))

        self.assertEqual(round(func.trap_reimann(0, 3, 1), 7), 52.7556198, f"Should be 52.7556198")
        self.assertEqual(round(func.trap_reimann(0, 3, 2), 7), 36.1037118, f"Should be 36.7037118")


if __name__ == '__main__':
    unittest.main()