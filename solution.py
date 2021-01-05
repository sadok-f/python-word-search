import multiprocessing
import random


class Solution:
    initial_board = [[]]
    board_1x_dict = {}
    directions = {
        'col+': [0, 1],
        'col-': [0, -1],
        'row+': [1, 0],
        'row-': [-1, 0],
        'row+col+': [1, 1],
        'row-col+': [-1, 1],
        'row-col-': [-1, -1],
        'row+col-': [1, -1]
    }

    def __init__(self, board_size):
        self.initial_board = self.generate_multi_dimension_board(board_size)
        self.board_1x_dict = self.to_one_dimension_dict(self.initial_board)

    def generate_multi_dimension_board(self, board_size):
        """Generate Multi-Dimenstional Board contains random letters"""
        letters = 'abcdefghijklmnopqrstuvwxyz'

        return [[random.choice(letters) for i in range(board_size)] for j in range(board_size)]

    @staticmethod
    def to_one_dimension_dict(board):
        """Convert given multidimensional list to one dimension dict"""
        return {(i, j): val
                for i, row in enumerate(board)
                for j, val in enumerate(row)}

    def words_search(self, words):
        """Search all valid words for given board, it uses multiprocessing to find the valid words"""

        print(f' CPU count: {multiprocessing.cpu_count()}')

        with multiprocessing.Pool() as pool:
            return pool.map(self.search_by_word, words)

    def search_by_word(self, word):
        """Search given word if exist in given board, return the word if exist, False if not"""
        len_word = len(word)
        first_letter = word[0] if len_word > 0 else ''
        for coordinate, letter in self.board_1x_dict.items():
            if len_word > 0 and letter == first_letter:
                if self.search_word_by_position(word, coordinate):
                    return word
        return False

    def search_word_by_position(self, word, coordinate, position=0, orientation=''):
        """Search given word position if it exist withing the given coordinate, and checks in 8 directions"""
        if coordinate not in self.board_1x_dict.keys():
            return False

        if word[position] != self.board_1x_dict[coordinate]:
            return False

        if position + 1 == len(word) and word[position] == self.board_1x_dict[coordinate]:
            return True

        for direction, pos in self.directions.items():
            if (orientation == direction) or orientation == '':
                (row, col) = coordinate
                if self.search_word_by_position(word,
                                                (row + pos[0], col + pos[1]),
                                                position + 1, direction):
                    return True
