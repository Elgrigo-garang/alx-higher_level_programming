#!/usr/bin/python3
"""Define a text file-raeding function."""

def read_file(filename=""):
    """print the content of a UTF8 text file to stdout"""
    with open(filename, encodings="utf-8") as f:
        print(f.read(), end="")
