import time
import argparse
from solution import Solution


def read_words_from_file(file_path):
    """Return list of words from given file path"""
    my_file = open(file_path, "r")
    file_data = my_file.readlines()
    # Remove "\n" in at the end of each word
    return list(map(lambda word: word[:-1], file_data))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python script that searches a grid of random generated letters for valid words")
    parser.add_argument("--size", "-s", help="Set the board size", required=True)
    parser.add_argument("--file", "-f", help="Path to file contains list of words", required=True)
    args = parser.parse_args()
    parser.parse_args()
    # instantiate Solution class
    solution = Solution(int(args.size))
    valid_words = read_words_from_file(args.file)

    # Printing the generated Board
    for x in solution.initial_board:
        print(x)

    start = time.perf_counter()
    # Searching the words
    results = solution.words_search(valid_words)
    # Remove False outputs from results
    result = [x for x in results if x is not False]

    print(f' Count of valid words: {len(result)}')
    print(f' List of valid words: {result}')

    finish = time.perf_counter()
    print(f' Finished in {round(finish - start, 2)} second(s)')
