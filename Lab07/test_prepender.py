from unittest import TestCase
from A01166243_1510_labs.Lab07.midterm import prepender


class TestPrepender(TestCase):
    def test_prepender_empty_list_empty_string(self):
        empty_list = []
        zero_string = ''
        prepender(empty_list, zero_string)
        self.assertEqual([], empty_list)

    def test_prepender_empty_list_python_string(self):
        empty_list = []
        python_string = 'Python'
        prepender(empty_list, python_string)
        self.assertEqual([], empty_list)

    def test_prepender_python_list_empty_string(self):
        python_list = ['Python']
        empty_string = ''
        prepender(python_list, empty_string)
        self.assertEqual(['Python'], python_list)

    def test_prepender_python_list_i_love_string(self):
        python_list = ['Python']
        python_string = "I love "
        prepender(python_list, python_string)
        self.assertEqual(['I love Python'], python_list)

    def test_prepender_multi_list_empty_string(self):
        multi_list = ['Python', 'is', 'better', 'than', 'JavaScript']
        python_string = ""
        prepender(multi_list, python_string)
        self.assertEqual(['Python', 'is', 'better', 'than', 'JavaScript'], multi_list)

    def test_prepender_multi_list_umm_string(self):
        multi_list = ['Python', 'is', 'better', 'than', 'JavaScript']
        umm_string = "Umm... "
        prepender(multi_list, umm_string)
        self.assertEqual(['Umm... Python', 'Umm... is', 'Umm... better', 'Umm... than', 'Umm... JavaScript'],
                         multi_list)

