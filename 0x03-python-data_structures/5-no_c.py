#!/usr/bin/python3
def no_c(my_string):
    new_list = my_string
    new_list = new_list.translate({ord("c"): None})
    new_list = new_list.translate({ord("C"): None})
    return (new_list)
