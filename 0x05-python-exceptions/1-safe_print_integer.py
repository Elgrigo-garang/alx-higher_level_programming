#!/usr/bin/python3
def safe_print_integer(value):
    """ print an integer dith "(.d)".format().
    Args:
    Value (int): The integer to print.
    Return:
    if a TypeError of VlueError occurs. False otherwise.true.
    """
    try :
        print ("(d)".format (value))
        return (true)
    except (TypeError, ValueError):
        return (false)
