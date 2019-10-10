from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import generate_vowel
import random


class TestGenerateVowel(TestCase):
    def test_generate_vowel_1(self):
        random.seed(23)
        self.assertEqual(['I'], generate_vowel())

    def test_generate_vowel_2(self):
        random.seed(61)
        self.assertEqual(['O'], generate_vowel())

    def test_generate_vowel_3(self):
        random.seed(37)
        self.assertEqual(['Y'], generate_vowel())
