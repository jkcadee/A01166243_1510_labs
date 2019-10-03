from unittest import TestCase
from A01166243_1510_labs.Lab04.time_calculator import time_calculator


class TestTimeCalculator(TestCase):
    def test_time_calculator(self):
        self.assertEqual('0 days, 0 hours, 0 minutes, 0 seconds.', time_calculator(0))
        self.assertEqual('0 days, 0 hours, 0 minutes, 59 seconds.', time_calculator(59))
        self.assertEqual('0 days, 0 hours, 1 minutes, 0 seconds.', time_calculator(60))
        self.assertEqual('0 days, 0 hours, 59 minutes, 59 seconds.', time_calculator(3599))
        self.assertEqual('0 days, 1 hours, 0 minutes, 0 seconds.', time_calculator(3600))
        self.assertEqual('0 days, 23 hours, 59 minutes, 59 seconds.', time_calculator(86399))
        self.assertEqual('1 days, 0 hours, 0 minutes, 0 seconds.', time_calculator(86400))
        self.assertEqual('1 days, 0 hours, 0 minutes, 1 seconds.', time_calculator(86401))
