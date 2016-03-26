#!/usr/bin/env python
from nodes import Node

class Divide(Node):
    """
    Takes two items from the stack and divides them
    """
    char = "/"
    args = 2
    results = 1
    def func(self, a,b):
        """a/b. floating point division.
For integer division, see `f`"""
        return a/b