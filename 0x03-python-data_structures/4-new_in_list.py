#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = [];
    if idx > 0 and idx < (len(my_list) - 1):
        for i, e in enumerate(my_list):
            if i != idx:
                list.append(e)
            else:
                list.append(element)
        return (list)
    else:
        return (my_list)
