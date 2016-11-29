#!/usr/bin/env python

from node.sort import Sort
from nodes import Node


class Tail(Node):
    char = "t"
    args = 1
    results = 1
    contents = ["seconds", "minutes", "hours", "days", "weeks", "months", "years", "decades", "centuries", "millenia"]
    
    @Node.test_func([2], [1])
    def decrement(self, inp: Node.number):
        """inp-1"""
        return inp-1
    
    @Node.test_func([[1, 2, 3]], [[2, 3]])
    def first(self, inp: Node.indexable):
        """inp[1:]"""
        return [inp[1:]]
    
    @Node.test_func([Node.clock.default_time], [Node.clock.default_time])
    def time(self, time:Node.clock):
        time.defined_values[:3] = [False]*3
        return time
    
    @Node.test_func([{1:1, "2":2}], [[[1, 1], ['2', 2]]])
    def items(self, inp: dict):
        """sorted(inp.items)"""
        return [[list(i)for i in Sort.sort_list(inp.items())]]

    def inf_tail(self, inf: Node.infinite):
        next(inf)
        return inf