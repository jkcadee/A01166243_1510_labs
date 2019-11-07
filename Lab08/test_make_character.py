from unittest import TestCase
from A01166243_1510_labs.Lab08.maze import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_zero(self):
        self.assertEqual([0, 0], make_character(0, 0))

    def test_make_character_zero_one(self):
        self.assertEqual([0, 1], make_character(0, 1))

    def test_make_character_one_zero(self):
        self.assertEqual([1, 0], make_character(1, 0))

    def test_make_character_one_one(self):
        self.assertEqual([1, 1], make_character(1, 1))

    def test_make_character_five_five(self):
        self.assertEqual([5, 5], make_character(5, 5))
