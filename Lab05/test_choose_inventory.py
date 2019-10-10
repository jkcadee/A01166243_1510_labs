from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import choose_inventory
import random


random.seed(3)


class TestChooseInventory(TestCase):
    def test_choose_inventory_1(self):
        self.assertEqual(['Dagger', 'Sword'], choose_inventory(['Sword', 'Dagger', 'Chainmail'], 2))

    def test_choose_inventory_empty(self):
        self.assertEqual([], choose_inventory([], 2))

    def test_choose_inventory_over(self):
        self.assertEqual(['Sword'], choose_inventory(['Sword'], 2))

    def test_choose_inventory_equal(self):
        self.assertEqual(['Sword'], choose_inventory(['Sword'], 1))
