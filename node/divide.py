#!/usr/bin/env python
from nodes import Node

#Divide
@Node.test("/", [2,4], [2])
@Node.test("/", [4,2], [0.5])
#Count
@Node.test("/", ["t", "test"], [2])
@Node.test("/", [3, (3,1,2,1,3)], [2])
class Divide(Node):
    """
    Takes two items from the stack and divides them
    """
    char = "/"
    args = 2
    results = 1
    def func(self, a: Node.number, b: Node.number):
        """a/b. floating point division.
For integer division, see `f`"""
        return a/b
    
    def count(self, a: Node.indexable, b):
        """a.count(b)"""
        return a.count(b)
    