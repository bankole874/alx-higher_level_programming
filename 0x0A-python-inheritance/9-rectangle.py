#!/usr/bin/python3
""" Import module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Rectangle class inheirts from BaseGeometry. """


class Rectangle(BaseGeometry):

    """ constructor method """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """ Function area """
    def area(self):
        return (self.__width * self.__height)

    """ Returns Rectangle description """
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
