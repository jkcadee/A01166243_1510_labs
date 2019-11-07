from unittest import TestCase
from A01166243_1510_labs.Lab08.maze import make_board


class TestMakeBoard(TestCase):
    def test_make_board_zero(self):
        self.assertEqual([], make_board(0, 0))

    def test_make_board_one(self):
        self.assertEqual([[(0, 0)]], make_board(1, 1))

    def test_make_board_five(self):
        self.assertEqual([[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
                          [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
                          [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
                          [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
                          [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]], make_board(5, 5))
