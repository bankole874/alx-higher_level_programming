#!/usr/bin/python3
""" import module """
Rectangle = __import__('9-rectangle').Rectangle
""" Square inherits from Rectangle """


class Square(Rectangle):

    """ constructor method """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
