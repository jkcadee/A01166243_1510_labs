from unittest import TestCase


class TestRemainder_number(TestCase):
    def test_remainder_number(self):
        self.assertTrue(7 % 5, msg=None)
        self.assertTrue(-7 % -5, msg=None)
        self.assertTrue(-7 % 5, msg=None)
        self.assertTrue(7 % -5, msg=None)
