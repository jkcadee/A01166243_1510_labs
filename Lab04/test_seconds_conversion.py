from unittest import TestCase
from A01166243_1510_labs.Lab04.time_calculator import seconds_conversion


class TestSecondsConversion(TestCase):
    def test_seconds_conversion(self):
        self.assertEqual(10, seconds_conversion(600, 60))
        self.assertEqual(100, seconds_conversion(100, 1))
        self.assertEqual(2, seconds_conversion(6400 , 3600))

