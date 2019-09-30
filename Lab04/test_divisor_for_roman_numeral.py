from unittest import TestCase


class TestDivisor_for_roman_numeral(TestCase):
    def test_divisor_for_roman_numeral(self):
        self.assertTrue(10 / 5, msg=None)
        self.assertTrue(-10 / -5, msg=None)
        self.assertTrue(10 / -5, msg=None)
        self.assertTrue(-10 / 5, msg=None)
