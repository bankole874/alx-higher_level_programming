#!/usr/bin/python3
""" from int """


class MyInt(int):

    """ overridden method """
    def __eq__(self, other):
        return (int(self) != other)

    """ overridden method """
    def __ne__(self, other):
        return (int(self) == other)
