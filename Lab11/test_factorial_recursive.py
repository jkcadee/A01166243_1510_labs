from unittest import TestCase
from Lab11.lab_11_Kayden_and_Janelle import factorial_recursive


class TestFactorialRecursive(TestCase):
    def test_factorial_recursive_first(self):
        self.assertEqual(120, factorial_recursive(5))

    def test_factorial_recursive_second(self):
        self.assertEqual(1307674368000, factorial_recursive(15))

    def test_factorial_recursive_one(self):
        self.assertEqual(1, factorial_recursive(1))
