from unittest import TestCase
from A01166243_1510_labs.Lab04.roman_numbers import remainder_number

class TestRemainder_number(TestCase):
    def test_remainder_number(self):
        self.assertEqual(2, remainder_number(7, 5))
        self.assertEqual(-2, remainder_number(-7, -5))
        self.assertEqual(-3, remainder_number(7, -5))
        self.assertEqual(3, remainder_number(-7, 5))