#!/usr/bin/python3

"""define a atext file line-counting function."""


def number_of_lines(filename=""):
    """return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1

        return
