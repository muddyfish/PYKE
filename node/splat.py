#!/usr/bin/env python

from nodes import Node

class Str(Node):
    char = "X"
    args = 1
    results = None
    
    @Node.test_func([[2,3,4,1]], [2,3,4,1])
    def func(self, lst):
        """return lst (extend mode)"""
        return list(lst)