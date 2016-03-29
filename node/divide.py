#!/usr/bin/env python
from nodes import Node

class Divide(Node):
    """
    Takes two items from the stack and divides them
    """
    char = "/"
    args = 2
    results = 1
    
    
    @Node.test_func([4,2], [2])
    @Node.test_func([2,4], [0.5])
    def func(self, a: Node.number, b: Node.number):
        """a/b. floating point division.
For integer division, see `f`"""
        return a/b
    
    @Node.test_func(["test", "t"], [2])
    @Node.test_func([(3,1,2,1,3), 3], [2])
    def count(self, a: Node.indexable, b):
        """a.count(b)"""
        return a.count(b)
    