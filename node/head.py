#!/usr/bin/env python

from node.sort import Sort
from nodes import Node
from type.type_time import TypeTime


class Head(Node):
    char = "h"
    args = 1
    results = 1
    
    @Node.test_func([3], [4])
    def increment(self, inp: Node.number):
        """inp+1"""
        return inp+1
    
    @Node.test_func([[3, 2]], [3])
    @Node.test_func(["test"], ["t"])
    def first(self, inp: Node.indexable):
        """inp[0]"""
        return [inp[0]]

    def date(self, time: Node.clock):
        """return date part of time"""
        time.defined_values[3:] = [False]*3
        return TypeTime.parse_time_delta(time.get_rel_delta())
    
    @Node.test_func([{1: 1, "2": 2}], [[1, "2"]])
    def keys(self, inp: dict):
        """sorted(inp.keys)"""
        return [Sort.sort_list(inp.keys())]

    def inf_next(self, inf: Node.infinite):
        return next(inf)
