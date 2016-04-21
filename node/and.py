#!/usr/bin/env python

from nodes import Node

class And(Node):
    char = "&"
    args = 2
    results = 1
    
    @Node.test_func([2,1], [1])
    @Node.test_func([0,1], [False])
    @Node.test_func([4, "Hello!"], ["Hello!"])
    def func(self, a,b):
        """a and b. Short circuiting. If not b, return a."""
        return [a and b]