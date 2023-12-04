#!/usr/bin/env python3
def no_c(my_string):
    new_list = list(my_string)
    for i, e in enumerate(new_list):
        if (e == "c" or e == "C"):
            del new_list[i]
    return ("".join(new_list))
