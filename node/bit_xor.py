#!/usr/bin/env python

from nodes import Node

class BitXOR(Node):
    args = 2
    results = 1
    char = ".^"
    
    @Node.test_func([4,5], [1])
    def func(self, a,b):
        """a^b"""
        return a^b
