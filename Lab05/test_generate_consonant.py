from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import generate_consonant
import random


class TestGenerateConsonant(TestCase):
    def test_generate_consonant_1(self):
        random.seed(14)
        self.assertEqual(['F'], generate_consonant())

    def test_generate_consonant_2(self):
        random.seed(72)
        self.assertEqual(['D'], generate_consonant())

    def test_generate_consonant_3(self):
        random.seed(5)
        self.assertEqual(['Y'], generate_consonant())
