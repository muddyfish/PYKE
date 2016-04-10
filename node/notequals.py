#!/usr/bin/env python

from nodes import Node

class NotEquals(Node):
    char = "N"
    args = 2
    results = 1
    
    @Node.test_func([1,2], [1])
    @Node.test_func([1.0,1], [0])
    @Node.test_func(["test","test"], [0])
    def func(self, a,b):
        """a!=b. Returns an int"""
        return (a!=b)+0