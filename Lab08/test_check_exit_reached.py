from unittest import TestCase
from A01166243_1510_labs.Lab08.maze import check_exit_reached


class TestCheckExitReached(TestCase):
    def test_check_exit_reached_min_5_max_5(self):
        self.assertEqual([4, 4], check_exit_reached(5, 5))

    def test_check_exit_reached_min_1_max_5(self):
        self.assertEqual([0, 4], check_exit_reached(1, 5))

    def test_check_exit_reached_min_5_max_1(self):
        self.assertEqual([4, 0], check_exit_reached(5, 1))

    def test_check_exit_reached_min_0_max_0(self):
        self.assertEqual([-1, -1], check_exit_reached(0, 0))
