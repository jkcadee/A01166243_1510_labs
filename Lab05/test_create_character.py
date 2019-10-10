from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import create_character
import random


class TestCreateCharacter(TestCase):
    def test_create_character(self):
        random.seed(3)
        self.assertEqual(['Tuwoqy',
                          ['Strength:', 12],
                          ['Dexterity:', 10],
                          ['Constitution:', 15],
                          ['Intelligence:', 7],
                          ['Wisdom:', 12],
                          ['Charisma:', 10]], create_character(3))

    def test_create_character_length_0(self):
        random.seed(9107)
        self.assertEqual(['',
                          ['Strength:', 8],
                          ['Dexterity:', 10],
                          ['Constitution:', 10],
                          ['Intelligence:', 10],
                          ['Wisdom:', 9],
                          ['Charisma:', 12]], create_character(0))

    def test_create_character_length_negative(self):
        self.assertEqual('No strength of magic can make a name have less than zero characters.', create_character(-1))
