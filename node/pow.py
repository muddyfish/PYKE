#!/usr/bin/env python

from nodes import Node

class Pow(Node):
    """
    Takes two items from the stack and raises a^b
    """
    char = "^"
    args = 2
    results = 1
    
    def func(self, a: Node.number, b: Node.number):
        """a**b"""
        return a**b