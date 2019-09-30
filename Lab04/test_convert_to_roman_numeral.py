from unittest import TestCase
from A01166243_1510_labs.Lab04.roman_numbers import convert_to_roman_numeral

class TestConvert_to_roman_numeral(TestCase):
    def test_convert_to_roman_numeral(self):
        self.assertEqual('I', convert_to_roman_numeral(1))
        self.assertEqual('MMMMMMMMMM', convert_to_roman_numeral(10000))
        self.assertEqual('IV', convert_to_roman_numeral(4))
        self.assertEqual('IX', convert_to_roman_numeral(9))
        self.assertEqual('V', convert_to_roman_numeral(5))
        self.assertEqual('VI', convert_to_roman_numeral(6))
        self.assertEqual('X', convert_to_roman_numeral(10))
        self.assertEqual('XX', convert_to_roman_numeral(20))
        self.assertEqual('XL', convert_to_roman_numeral(40))
        self.assertEqual('L', convert_to_roman_numeral(50))
        self.assertEqual('LX', convert_to_roman_numeral(60))
        self.assertEqual('XC', convert_to_roman_numeral(90))
        self.assertEqual('C', convert_to_roman_numeral(100))
        self.assertEqual('CD', convert_to_roman_numeral(400))
        self.assertEqual('D', convert_to_roman_numeral(500))
        self.assertEqual('CM', convert_to_roman_numeral(900))
        self.assertEqual('M', convert_to_roman_numeral(1000))
        self.assertEqual('MMMMM', convert_to_roman_numeral(5000))

