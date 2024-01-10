#!/usr/bin/python3
"""
function add_attribute
"""


def add_attribute(cls, field, name):
    if hasattr(cls, "__dict__"):
        setattr(cls, field, name)
    else:
        raise TypeError("can't add new attribute")
