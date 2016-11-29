#!/usr/bin/env python

from node.sort import Sort
from nodes import Node


class Head(Node):
    char = "h"
    args = 1
    results = 1
    
    @Node.test_func([3], [4])
    def increment(self, inp: Node.number):
        """inp+1"""
        return inp+1
    
    @Node.test_func([[3,2]], [3])
    @Node.test_func(["test"], ["t"])
    def first(self, inp: Node.indexable):
        """inp[0]"""
        return [inp[0]]
    
    @Node.test_func([Node.clock.default_time], [Node.clock.default_time])
    def time(self, time:Node.clock):
        time.defined_values[3:] = [False]*3
        return time
    
    @Node.test_func([{1:1, "2":2}], [[1,"2"]])
    def keys(self, inp: dict):
        """sorted(inp.keys)"""
        return [Sort.sort_list(inp.keys())]

    def inf_next(self, inf: Node.infinite):
        return next(inf)