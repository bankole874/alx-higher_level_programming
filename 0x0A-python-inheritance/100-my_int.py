#!/usr/bin/python3
""" from int """

class MyInt(int):

    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
