#!/usr/bin/env python3
"""
Unit tests for the Python Calculator
"""

import unittest
from calculator import add, subtract, multiply, divide, power, square_root


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions"""

    def test_add(self):
        """Test addition"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        """Test multiplication"""
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        """Test division"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)

    def test_divide_by_zero(self):
        """Test division by zero"""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        """Test power function"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)

    def test_square_root(self):
        """Test square root"""
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.414213, places=5)

    def test_square_root_negative(self):
        """Test square root of negative number"""
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_square_root_zero(self):
        """Test square root of zero"""
        self.assertEqual(square_root(0), 0)


if __name__ == "__main__":
    unittest.main()
