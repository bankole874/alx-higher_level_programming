#!/usr/bin/python3
""" MyList function """


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
