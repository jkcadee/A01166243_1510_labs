from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import generate_name
import random


class TestGenerateName(TestCase):
    def test_generate_name_no_syllables(self):
        random.seed(0)
        self.assertEqual('', generate_name(0))

    def test_generate_name_1(self):
        random.seed(99)
        self.assertEqual('Qo', generate_name(1))

    def test_generate_name_2(self):
        random.seed(409)
        self.assertEqual('Vutewoza', generate_name(4))

    def test_generate_name_3(self):
        random.seed(581)
        self.assertEqual('Bemiqyburi', generate_name(5))
