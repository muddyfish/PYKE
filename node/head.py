#!/usr/bin/env python

from nodes import Node

class Head(Node):
    char = "h"
    args = 1
    results = 1
    
    @Node.test_func([3], [4])
    def add_one(self, inp: Node.number):
        """inp+1"""
        return inp+1
    
    @Node.test_func([[3,2]], [3])
    @Node.test_func(["test"], ["t"])
    def first(self, inp: Node.indexable):
        """inp[0]"""
        return [inp[0]]