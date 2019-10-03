from unittest import TestCase
from A01166243_1510_labs.Lab04.time_calculator import remainder_seconds


class TestRemainderSeconds(TestCase):
    def test_remainder_seconds(self):
        self.assertEqual(10, remainder_seconds(130, 60))
        self.assertEqual(100, remainder_seconds(3700, 3600))
        self.assertEqual(3600, remainder_seconds(90000, 86400))

