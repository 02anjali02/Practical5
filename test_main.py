import unittest
from main import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add_numbers(-5, -3)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        result = add_numbers(5, -3)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
