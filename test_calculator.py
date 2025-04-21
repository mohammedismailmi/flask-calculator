"""Unit tests for calculator logic"""

import unittest
from app import calculate

class TestCalculator(unittest.TestCase):
    """Test cases for calculation logic"""

    def test_addition(self):
        """Test addition"""
        self.assertEqual(calculate(10, 5, "add"), 15)

    def test_subtraction(self):
        """Test subtraction"""
        self.assertEqual(calculate(10, 5, "subtract"), 5)

    def test_multiplication(self):
        """Test multiplication"""
        self.assertEqual(calculate(10, 5, "multiply"), 50)

    def test_division(self):
        """Test division"""
        self.assertEqual(calculate(10, 5, "divide"), 2)

    def test_divide_by_zero(self):
        """Test divide by zero"""
        self.assertEqual(calculate(10, 0, "divide"), "Cannot divide by zero")

    def test_invalid_input(self):
        """Test invalid input"""
        self.assertEqual(calculate("a", 5, "add"), "Invalid input")

if __name__ == "__main__":
    unittest.main()
