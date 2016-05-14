#!/usr/bin/env python

from nodes import Node

class Splat(Node):
    char = "X"
    args = 1
    results = None
    
    @Node.test_func([[2,3,4,1]], [2,3,4,1])
    @Node.test_func(["hello"], ["h","e","l","l","o"])
    def func(self, a: Node.indexable):
        """return a (extend mode)"""
        return list(a)
    
    @Node.test_func([3], [9])
    def square(self, x: Node.number):
        """Return X squared"""
        return x**2
    