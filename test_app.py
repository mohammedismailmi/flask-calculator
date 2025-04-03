import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post("/", data={"num1": "5", "num2": "3", "operation": "add"})
        self.assertIn(b"8", response.data)

    def test_subtraction(self):
        response = self.app.post("/", data={"num1": "5", "num2": "3", "operation": "subtract"})
        self.assertIn(b"2", response.data)

    def test_multiplication(self):
        response = self.app.post("/", data={"num1": "5", "num2": "3", "operation": "multiply"})
        self.assertIn(b"15", response.data)

    def test_division(self):
        response = self.app.post("/", data={"num1": "6", "num2": "3", "operation": "divide"})
        self.assertIn(b"2", response.data)

    def test_division_by_zero(self):
        response = self.app.post("/", data={"num1": "6", "num2": "0", "operation": "divide"})
        self.assertIn(b"Cannot divide by zero", response.data)

if __name__ == "__main__":
    unittest.main()
