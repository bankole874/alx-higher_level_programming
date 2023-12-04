#!/usr/bin/env python3
def no_c(my_string):
    #list all files
    new_list = list(my_string)
    #iterate through the list to find c or C
    for i, e in enumerate(new_list):
        if (e == "c" or e == "C"):
            #remove the letter
            del new_list[i]
    return ("".join(new_list))
