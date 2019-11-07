from unittest import TestCase
from A01166243_1510_labs.Lab08.maze import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_move_valid_NS(self):
        self.assertEqual([0, 1], move_character([0, 0], 5, 1, 'S'))

    def test_move_character_move_not_valid_NS(self):
        self.assertEqual([0, 0], move_character([0, 0], 5, 1, 'N'))

    def test_move_character_move_valid_EW(self):
        self.assertEqual([1, 0], move_character([0, 0], 5, 0, 'E'))

    def test_move_character_move_not_valid_EW(self):
        self.assertEqual([0, 0], move_character([0, 0], 5, 1, 'W'))

    def test_move_character_move_valid_max_1_NS(self):
        self.assertEqual([0, 0], move_character([0, 0], 1, 1, 'S'))

    def test_move_character_move_valid_max_1_EW(self):
        self.assertEqual([0, 0], move_character([0, 0], 1, 1, 'E'))

    def test_move_character_empty_valid(self):
        self.assertEqual([1, 0], move_character([0, 0], 0, 0, 'S'))

    def test_move_character_empty_not_valid(self):
        self.assertEqual([0, 0], move_character([0, 0], 0, 0, 'N'))
