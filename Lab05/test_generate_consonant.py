from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import generate_consonant
import random


class TestGenerateConsonant(TestCase):
    def test_is_consonant_is_in(self):
        consonant = "BCDFGHJKLMNPQRSTVWXYZ"
        self.assertTrue(''.join(generate_consonant()) in consonant)

    def test_is_consonant_length(self):
        self.assertTrue(len(generate_consonant()) == 1, generate_consonant())
