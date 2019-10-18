from unittest import TestCase
from A01166243_1510_labs.Lab06.sparsevector import sparse_add


class TestSparseAdd(TestCase):
    def test_sparse_add_2_empty_dict(self):
        self.assertEqual({}, sparse_add({}, {}))

    def test_sparse_add_1_empty_dict1(self):
        self.assertEqual({4: 5, 6: 7}, sparse_add({4: 5, 6: 7}, {}))

    def test_sparse_add_1_empty_dict2(self):
        self.assertEqual({1: 2, 9: 2}, sparse_add({}, {1: 2, 9: 2}))

    def test_sparse_add_same_index(self):
        self.assertEqual({1: 2, 7: 3, 9: 7}, sparse_add({1: 1, 7: 2, 9: 3}, {1: 1, 9: 4, 7: 1}))

    def test_sparse_add_no_same_index(self):
        self.assertEqual({1: 3, 2: 1, 6: 9, 9: 6}, sparse_add({1: 3, 6: 9}, {2: 1, 9: 6}))

    def test_sparse_add_some_same_index(self):
        self.assertEqual({1: 3, 2: 11, 5: 5, 6: 6}, sparse_add({1: 3, 5: 2, 6: 3}, {2: 11, 5: 3, 6: 3}))

    def test_sparse_add_to_zero(self):
        self.assertEqual({}, sparse_add({1: 3}, {1: -3}))
