import unittest
from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import choose_inventory
from unittest.mock import patch
import io

inventory = ['Sword', 'Dagger', 'Chainmail']


class TestChooseInventory(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_print_negative(self, mock_stdout):
        output = "Hey! You can't have negative items!\n"
        choose_inventory([inventory], -1)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_choose_inventory_empty(self):
        self.assertEqual([], choose_inventory([], 2))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_print_over(self, mock_stdout):
        output = "You are over encumbered.\n"
        choose_inventory([inventory], 4)
        self.assertEqual(mock_stdout.getvalue(), output)

    def test_choose_inventory_over(self):
        self.assertEqual([inventory], choose_inventory([inventory], 2))

    def test_choose_inventory_equal(self):
        self.assertEqual([inventory], choose_inventory([inventory], 1))
