#!/usr/bin/python3
""" BaseGeometry class. """


class BaseGeometry():

    """ Raises an Excpetion because area is not implemented """
    def area(self):

        raise Exception("area() is not implemented")
    """
    Validates a value...
    if value is not an integer: raise a TypeError exception.
    if value is less or equal to 0: raise a ValueError
    """
    def integer_validator(self, name, value):

        if (type(value) is not int):
            raise TypeError(name + " must be an integer")
        if (value <= 0):
            raise ValueError(name + " must be greater than 0")
