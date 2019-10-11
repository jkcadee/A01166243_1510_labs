from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import print_character, create_character
import unittest.mock
import io


@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class TestPrintCharacter(TestCase):
    def test_print_character_name(self, mock_stdout):
        name = ['Panini']
        output = 'Panini\n'
        print_character(name)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_print_character_str(self, mock_stdout):
        stren = ['Strength: 6']
        output = 'Strength: 6\n'
        print_character(stren)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_print_character_dex(self, mock_stdout):
        dex = ['Dexterity: 12']
        output = 'Dexterity: 12\n'
        print_character(dex)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_print_character_const(self, mock_stdout):
        const = ['Constitution: 13']
        output = 'Constitution: 13\n'
        print_character(const)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_print_character_int(self, mock_stdout):
        intel = ['Intelligence: 16']
        output = 'Intelligence: 16\n'
        print_character(intel)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_print_character_wis(self, mock_stdout):
        wis = ['Wisdom: 10']
        output = 'Wisdom: 10\n'
        print_character(wis)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_print_character_char(self, mock_stdout):
        char = ['Charisma: 12']
        output = 'Charisma: 12\n'
        print_character(char)
        self.assertEqual(mock_stdout.getvalue(), output)
