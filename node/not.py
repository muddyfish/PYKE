#!/usr/bin/env python

from nodes import Node

class Not(Node):
    char = "!"
    args = 1
    results = 1
    
    
    @Node.test_func([1], [0])
    @Node.test_func([""], [1])
    @Node.test_func([0], [1])
    def func(self, a):
        """if a: return 0
else: return 1

Non-truthy values: 0, 0.0, "", [], (), {}, set()"""
        return (not a)+0