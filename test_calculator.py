import unittest
from app import calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(10, 5, "add"), 15)

    def test_subtract(self):
        self.assertEqual(calculate(10, 5, "subtract"), 5)

    def test_multiply(self):
        self.assertEqual(calculate(10, 5, "multiply"), 50)

    def test_divide(self):
        self.assertEqual(calculate(10, 5, "divide"), 2)

    def test_divide_by_zero(self):
        self.assertEqual(calculate(10, 0, "divide"), "Cannot divide by zero")

    def test_invalid_input(self):
        self.assertEqual(calculate("a", 5, "add"), "Invalid input")

if __name__ == '__main__':
    unittest.main()
