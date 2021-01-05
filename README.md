# python-word-search

a Python program that searches a grid of letters (a-z only) for valid English words.

Words can be found along any diagonal, forwards, upwards, downwards or backwards and must not wrap’ between edges.

## requirement:

- Python 3.4+
- Pytest 6+

## Usage

```sh
python main.py -s 15 -f valid_words.txt
```

Where `-s` is the size of the board to be generated that contains random letters.

## Arguments

```
  -s SIZE, --size SIZE Set the board size
  -f FILE, --file FILE Path to file contains list of words
```

## Unit Tests

```sh
pytest
```