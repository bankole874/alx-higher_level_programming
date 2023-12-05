#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (my_list):
        id = 0
        size = len(my_list)
        bool_list = [False] * size
        for e in my_list:
            if (e % 2 == 0):
                bool_list[id] = True
            id += 1
        return (bool_list)
    return (list())
