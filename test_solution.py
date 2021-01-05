from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    words_board = [['a', 'b', 'a', 'c', 'a'],
                   ['d', 'b', 'c', 'c', 'e'],
                   ['e', 'a', 'a', 'e', 'e'],
                   ['a', 'b', 'c', 'b', 'a'],
                   ['d', 'a', 'e', 'b', 'd']
                   ]

    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(*args, **kwargs)
        self.solution = Solution(5)
        self.solution.initial_board = self.words_board
        self.solution.board_1x_dict = self.solution.to_one_dimension_dict(self.words_board)

    def test_words_search(self):
        words = ['abaca', 'adead', 'dbead', 'ababd', 'eba', 'eeca', 'abe', 'eaaee', 'daeb']
        assert self.solution.words_search(words) == words

    def test_words_search_not_wrap(self):
        words = ['ccbb', 'cae']
        assert self.solution.words_search(words) == [False, False]

    def test_words_search_longer_word(self):
        words = ['abacaaba']
        assert self.solution.words_search(words) == [False]

    def test_search_by_word(self):
        word = 'acabd'
        assert self.solution.search_by_word(word)

    def test_search_word_by_position_forward(self):
        word = 'eaaee'
        assert self.solution.search_word_by_position(word, (2, 0), 0, 'col+')

    def test_search_word_by_position_backward(self):
        word = 'abcba'
        assert self.solution.search_word_by_position(word, (3, 4), 0, 'col-')

    def test_search_word_by_position_downward(self):
        word = 'bbaba'
        assert self.solution.search_word_by_position(word, (0, 1), 0, 'row+')

    def test_search_word_by_position_upward(self):
        word = 'daeea'
        assert self.solution.search_word_by_position(word, (4, 4), 0, 'row-')

    def test_search_word_by_position_diagonal_up_forward(self):
        word = 'dbaca'
        assert self.solution.search_word_by_position(word, (4, 0), 0, 'row-col+')

    def test_search_word_by_position_diagonal_up_backward(self):
        word = 'dbaba'
        assert self.solution.search_word_by_position(word, (4, 4), 0, 'row-col-')

    def test_search_word_by_position_diagonal_down_backward(self):
        word = 'ababd'
        assert self.solution.search_word_by_position(word, (0, 0), 0, 'row+col+')

    def test_search_word_by_position_diagonal_down_forward(self):
        word = 'acabd'
        assert self.solution.search_word_by_position(word, (0, 4), 0, 'row+col-')
