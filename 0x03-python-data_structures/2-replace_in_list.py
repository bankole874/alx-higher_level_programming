#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list = []
    for i, e in enumerate(my_list):
        if i == idx:
            my_list[idx] = element
    return (my_list)
