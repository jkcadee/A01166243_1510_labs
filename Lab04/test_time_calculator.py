from unittest import TestCase
from A01166243_1510_labs.Lab04.time_calculator import time_calculator


class TestTimeCalculator(TestCase):
    def test_time_calculator_0(self):
        self.assertEqual('0 days, 0 hours, 0 minutes, 0 seconds.', time_calculator(0))

    def test_time_calculator_59(self):
        self.assertEqual('0 days, 0 hours, 0 minutes, 59 seconds.', time_calculator(59))

    def test_time_calculator_60(self):
        self.assertEqual('0 days, 0 hours, 1 minutes, 0 seconds.', time_calculator(60))

    def test_time_calculator_3599(self):
        self.assertEqual('0 days, 0 hours, 59 minutes, 59 seconds.', time_calculator(3599))

    def test_time_calculator_3600(self):
        self.assertEqual('0 days, 1 hours, 0 minutes, 0 seconds.', time_calculator(3600))

    def test_time_calculator_86399(self):
        self.assertEqual('0 days, 23 hours, 59 minutes, 59 seconds.', time_calculator(86399))

    def test_time_calculator_86400(self):
        self.assertEqual('1 days, 0 hours, 0 minutes, 0 seconds.', time_calculator(86400))

    def test_time_calculator_86401(self):
        self.assertEqual('1 days, 0 hours, 0 minutes, 1 seconds.', time_calculator(86401))

