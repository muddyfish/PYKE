#!/usr/bin/env python

from nodes import Node

class Add(Node):
    """
    Takes two items from the stack and adds them
    """
    char = "+"
    args = 2
    results = 1
    def func(self, a,b):
        return a+b