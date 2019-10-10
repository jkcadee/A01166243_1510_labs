from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import generate_syllable
import random


class TestGenerateSyllable(TestCase):
    def test_generate_syllable_1(self):
        random.seed(8)
        self.assertEqual(['K', 'I'], generate_syllable())

    def test_generate_syllable_2(self):
        random.seed(55)
        self.assertEqual(['D', 'E'], generate_syllable())

    def test_generate_syllable_3(self):
        random.seed(70)
        self.assertEqual(['F', 'I'], generate_syllable())
