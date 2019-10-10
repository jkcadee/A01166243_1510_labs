from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import print_character
import random
import unittest.mock
import io


@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class TestPrintCharacter(TestCase):
    def test_print_character(self, mock_stdout):
        random.seed(75)
        output = ['Lity', ['Strength:', 13], ['Dexterity:', 11], ['Constitution:', 17], ['Intelligence:', 16], ['Wisdom:', 10], ['Charisma:', 10], ['Dagger', 'Sword']]
        print_character(2, ['Sword', 'Dagger'], 2)
        self.assertEqual(mock_stdout.getvalue(), output)
