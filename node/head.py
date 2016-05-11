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
    
    @Node.test_func([Node.clock.default_time], [Node.clock.default_time])
    def time(self, time:Node.clock):
        time.hour = 0
        time.min = 0
        time.sec = 0
        return time