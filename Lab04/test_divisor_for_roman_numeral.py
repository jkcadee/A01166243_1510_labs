from unittest import TestCase
from A01166243_1510_labs.Lab04.roman_numbers import divisor_for_roman_numeral


class TestDivisorForRomanNumeral(TestCase):
    def test_divisor_for_roman_numeral(self):
        self.assertEqual(2, divisor_for_roman_numeral(10, 5))
        self.assertEqual(100, divisor_for_roman_numeral(1000, 10))
        self.assertEqual(6, divisor_for_roman_numeral(400, 60))
