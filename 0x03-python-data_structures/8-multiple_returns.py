#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence):
        size = len(sentence)
        letter1 = sentence[0]
        return ((size, letter1))
    return ((0, None))
