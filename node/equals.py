#!/usr/bin/env python

from nodes import Node

class Equals(Node):
    char = "q"
    args = 2
    results = 1
    
    @Node.test_func([1,2], [0])
    @Node.test_func([1.0,1], [1])
    @Node.test_func(["test","test"], [1])
    def func(self, a,b):
        """a==b. Returns an int"""
        return (a==b)+0