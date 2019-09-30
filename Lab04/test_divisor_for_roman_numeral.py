from unittest import TestCase
from A01166243_1510_labs.Lab04.roman_numbers import divisor_for_roman_numeral

class TestDivisor_for_roman_numeral(TestCase):
    def test_divisor_for_roman_numeral(self):
        self.assertEqual(2, divisor_for_roman_numeral(10, 5))
        self.assertEqual(2, divisor_for_roman_numeral(-10, -5))
        self.assertEqual(-2, divisor_for_roman_numeral(10, -5))
        self.assertEqual(-2, divisor_for_roman_numeral(-10, 5))

