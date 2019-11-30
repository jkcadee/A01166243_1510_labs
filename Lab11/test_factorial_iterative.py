from unittest import TestCase
from Lab11.lab_11_Kayden_and_Janelle import factorial_iterative


class TestFactorialIterative(TestCase):
    def test_factorial_iterative_first(self):
        self.assertEqual(120, factorial_iterative(5))

    def test_factorial_iterative_second(self):
        self.assertEqual(1307674368000, factorial_iterative(15))

    def test_factorial_iterative_one(self):
        self.assertEqual(1, factorial_iterative(1))
