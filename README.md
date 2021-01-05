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

### Arguments

```
  -s SIZE, --size SIZE Set the board size
  -f FILE, --file FILE Path to file contains list of valid words
```

## Unit Tests

```sh
pytest
```