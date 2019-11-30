from unittest import TestCase
from Lab11.lab_11_Kayden_and_Janelle import factorial_recursive_helper


class TestFactorialRecursiveHelper(TestCase):
    def test_factorial_recursive_helper_first(self):
        self.assertEqual(120, factorial_recursive_helper(5))

    def test_factorial_recursive_helper_second(self):
        self.assertEqual(1307674368000, factorial_recursive_helper(15))

    def test_factorial_recursive_helper_one(self):
        self.assertEqual(1, factorial_recursive_helper(1))
