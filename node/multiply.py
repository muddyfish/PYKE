#!/usr/bin/env python

from nodes import Node

class Multiply(Node):
    char = "*"
    args = 2
    results = 1
    
    @Node.test_func([4,5], [20])
    def func(self, a,b):
        """a*b"""
        return a*b