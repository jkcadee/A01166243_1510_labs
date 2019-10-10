from unittest import TestCase
import random

from A01166243_1510_labs.Lab05.Lab05 import roll_die

random.seed(4)


class TestRollDie(TestCase):
    def test_roll_die_1(self):
        self.assertEqual(2, roll_die(1, 6))

    def test_roll_die_2(self):
        self.assertEqual(10, roll_die(3, 6))

    def test_roll_die_3(self):
        self.assertEqual(20, roll_die(4, 8))
