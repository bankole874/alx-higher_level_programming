#!/usr/bin/python3
""" function is_kind_of _class """


def is_kind_of_class(obj, a_class):
    """
    True if the object is an instance of a_class
    if the object is an instance of a class that inherited from a_class,
    otherwise False.
    """
    return (isinstance(obj, a_class))
