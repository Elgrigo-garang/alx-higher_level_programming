#!/usr/bin/python3
def uppercase(str):
    for character in str:
        upper_str = ""
        asc = ord(character)
        if asc > 96 and asc < 123:
            upper_str += chr(asc - 32)
        else:
            upper_str += chr(asc)
        print('{}'.format(upper_str), end="")
    print()
