from unittest import TestCase
from A01166243_1510_labs.Lab08.maze import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_valid_NS(self):
        self.assertEqual([1, 0], validate_move(5, [0, 0], 'S'))

    def test_validate_move_not_valid_NS(self):
        self.assertEqual([0, 0], validate_move(5, [0, 0], 'N'))

    def test_validate_move_valid_EW(self):
        self.assertEqual([0, 1], validate_move(5, [0, 0], 'E'))

    def test_validate_move_not_valid_EW(self):
        self.assertEqual([0, 0], validate_move(5, [0, 0], 'W'))

    def test_validate_move_valid_diff_space_N(self):
        self.assertEqual([1, 2], validate_move(5, [2, 2], 'N'))

    def test_validate_move_valid_diff_space_W(self):
        self.assertEqual([2, 1], validate_move(5, [2, 2], 'W'))

    def test_validate_move_max_1_NS(self):
        self.assertEqual([0, 0], validate_move(1, [0, 0], 'S'))

    def test_validate_move_max_1_EW(self):
        self.assertEqual([0, 0], validate_move(1, [0, 0], 'E'))