#!/usr/bin/env python

from nodes import Node

class BitAnd(Node):
    char = ".&"
    args = 2
    results = 1
    
    @Node.test_func([4,5], [4])
    def func(self, a:int,b:int):
        """a&b"""
        return a&b
