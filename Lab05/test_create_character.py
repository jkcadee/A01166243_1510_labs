from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import create_character


class TestCreateCharacter(TestCase):
    def test_create_character_name(self):
        name = create_character(2)
        self.assertTrue(isinstance(name[0], str))

    def test_create_character_str(self):
        name = create_character(2)
        self.assertTrue(isinstance(name[1], list))

    def test_create_character_dex(self):
        name = create_character(2)
        self.assertTrue(isinstance(name[2], list))

    def test_create_character_const(self):
        name = create_character(2)
        self.assertTrue(isinstance(name[3], list))

    def test_create_character_int(self):
        name = create_character(2)
        self.assertTrue(isinstance(name[4], list))

    def test_create_character_wis(self):
        name = create_character(2)
        self.assertTrue(isinstance(name[5], list))

    def test_create_character_char(self):
        name = create_character(2)
        self.assertTrue(isinstance(name[6], list))

