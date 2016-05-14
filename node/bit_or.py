#!/usr/bin/env python

from nodes import Node

class BitOr(Node):
    char = ".|"
    args = 2
    results = 1
    
    @Node.test_func([4,1], [5])
    def func(self, a:int,b:int):
        """a|b"""
        return a|b