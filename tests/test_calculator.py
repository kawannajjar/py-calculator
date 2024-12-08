import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
    
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == '__main__':
    unittest.main()