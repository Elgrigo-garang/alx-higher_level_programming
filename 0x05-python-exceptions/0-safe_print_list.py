#!/usr/bin/pythoni3
def safe_print_list(my_list=[], x=0):
    """ print x elements of a list.
    Args:
    my_list (list): The lisst to print elements from
    x (int):The numbervof elements of my_list to print
    Returns:
    The number of elements printed.
    """
    ret = 0
    for i in range (x):
        try:
            print ("()".format (my_list [i], end = " "))
            ret += 1
        except IndexError:
            break
        print (" ")
        return (ret)
