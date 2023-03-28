#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ print the list x elements of a list that are integers
    Args:
    my_list (list): The list to print elelents from.
    x (int): the number of elementsof my_list to print
    Returns:
    The number of elrmrnts to be printed.
    """
    ret = 0
    for i in range (0, x):
        try:
            print ("(d)".format (my_list [i], end =" "))
            ret += 1
        except (ValueError, TypeError):
            continue:
                print (" ")
                return (ret)

