#!/usr/bin/env python

from nodes import Node

class FloorDiv(Node):
    char = "f"
    args = 2
    results = 1
    
    @Node.test_func([3,2], [1])
    @Node.test_func([6,-3], [-2])
    def func(self, a,b):
        """a/b. Rounds down, returns an int."""
        return a//b