import unittest
from calculator import add, subtract, multiply, divide

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

class TestSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 2), 3)
    
    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -2), -3)

class TestMultiply(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(4, 3), 12)
    
    def test_multiply_zero(self):
        self.assertEqual(multiply(5, 0), 0)

class TestDivide(unittest.TestCase):
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_zero(self):
        self.assertEqual(divide(10, 0), "Ошибка: деление на ноль")

if __name__ == "__main__":
    unittest.main()
