#!/usr/bin/env python
from nodes import Node

class Divide(Node):
    """
    Takes two items from the stack and divides them
    """
    char = "/"
    args = 2
    results = 1
    
    
    @Node.test_func([4,2], [2])
    @Node.test_func([2,4], [0.5])
    def func(self, a: Node.number, b: Node.number):
        """a/b. floating point division.
For integer division, see `f`"""
        return a/b
    
    @Node.test_func(["test", "t"], [2])
    @Node.test_func([(3,1,2,1,3), 3], [2])
    def count(self, a: Node.indexable, b):
        """a.count(b)"""
        return a.count(b)

    @Node.test_func([[4, 4, 2, 2, 9, 9], [1, 2, 3]], [[[4], [4, 2], [2, 9, 9]]])
    def split_length(self, inp: Node.indexable, lengths: Node.sequence):
        """Split inp into sections length lengths"""
        rtn = [[]]
        cur_length = 0
        for i in inp:
            if cur_length != len(lengths) and len(rtn[-1]) == lengths[cur_length]:
                cur_length += 1
                rtn.append([])
            rtn[-1].append(i)
        return [rtn]

    def time_int_div(self, a: Node.clock, b: Node.number):
        return a.divide_int(b)

    def time_int_div_2(self, a: Node.number, b: Node.clock):
        return b.divide_int(a)

    def time_div(self, a: Node.clock, b: Node.clock):
        return b.divide_time(a)