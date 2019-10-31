from unittest import TestCase
from A01166243_1510_labs.Lab07.midterm import cutoff


class TestCutoff(TestCase):
    def test_cutoff_empty_0(self):
        self.assertEqual(0, cutoff([], 0))

    def test_cutoff_empty_5(self):
        self.assertEqual(0, cutoff([], 5))

    def test_cutoff_zero_0(self):
        with self.assertRaises(ZeroDivisionError):
            cutoff([0], 0)

    def test_cutoff_zero_5(self):
        self.assertEqual(0, cutoff([0], 5))

    def test_cutoff_two_2(self):
        self.assertEqual(1, cutoff([2], 2))

    def test_cutoff_two_4(self):
        self.assertEqual(0, cutoff([2], 4))

    def test_cutoff_five_len_list_0(self):
        with self.assertRaises(ZeroDivisionError):
            cutoff([1, 2, 3, 4, 5], 0)

    def test_cutoff_five_len_list_2(self):
        self.assertEqual(2, cutoff([1, 2, 3, 4, 5], 2))

    def test_cutoff_five_len_list_2_2(self):
        self.assertEqual(5, cutoff([2, 2, 2, 2, 2], 2))

    def test_cutoff_five_len_list_2_10(self):
        self.assertEqual(2, cutoff([2, 2, 2, 2, 2], 10))

    def test_cutoff_five_len_list_3_3(self):
        self.assertEqual(5, cutoff([3, 6, 9, 12, 15], 3))


