#!/usr/bin/python3

"""define file pending function"""


def append_write(filename="", text=""):
    """appends to a string of a UTF8 text file.
    args:
    filename (str):the name of the file to append to.
    text (str):the string to append to
    Returns:
    the number of character to appended.
    """
    with open(fileame, "a", encoding="utf-8") as f:
        return f.write(text)
