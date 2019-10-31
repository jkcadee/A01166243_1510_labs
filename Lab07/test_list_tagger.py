from unittest import TestCase
from A01166243_1510_labs.Lab07.midterm import list_tagger


class TestListTagger(TestCase):
    def test_list_tagger_empty_list(self):
        self.assertEqual([0], list_tagger([]))

    def test_list_tagger_length_1(self):
        self.assertEqual([1, 2], list_tagger([2]))

    def test_list_tagger_multi_items(self):
        self.assertEqual([3, 1, 2, 4], list_tagger([1, 2, 4]))
