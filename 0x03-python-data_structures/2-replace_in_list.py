#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list = []
    for i, e in enumerate(my_list):
        if i != idx:
            list.append(e)
        else:
            list.append(element)
    my_list[idx] = element
    return (list)
