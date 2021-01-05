from unittest import TestCase

from main import *


class TestMain(TestCase):

    def test_read_words_from_file(self):
        words = read_words_from_file("valid_words.txt")
        assert len(words) > 0
