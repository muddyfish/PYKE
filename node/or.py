#!/usr/bin/env python

from nodes import Node

class Or(Node):
    char = "|"
    args = 2
    results = 1
    
    @Node.test_func([2,1], [2])
    @Node.test_func([3,0], [3])
    @Node.test_func([0,1], [1])
    @Node.test_func(["",""], [0])
    def func(self, a,b):
        """a or b. Short circuiting.
if a: return a
if b: return b
return 0"""
        if a: return [a]
        if b: return [b]
        return 0