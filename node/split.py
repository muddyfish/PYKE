#!/usr/bin/env python

import time

from nodes import Node


class Split(Node):
    char = "c"
    args = 2
    results = 1
    contents = "bcdfghjklmnpqrstvwxz"
    
    def prepare(self, stack):
        if len(stack) == 0:
            self.args = 1
            self.add_arg(stack)
        if isinstance(stack[0], Node.sequence):
            self.args = 1
    
    @Node.test_func(["1 2 1", " "], [["1", "2", "1"]])
    @Node.test_func(["1,3,4", ","], [["1", "3", "4"]])
    def split(self, inp: str, split: str):
        """inp.split(`arg`)"""
        return [inp.split(split)]
    
    @Node.test_func(["134", 1], [["1", "3", "4"]])
    @Node.test_func(["1234", 2], [["12", "34"]])
    def chunk(self, inp: Node.indexable, size: Node.number):
        """Return inp seperated into groups sized size"""
        size = float(size)
        rtn = []
        last = 0
        for i, val in enumerate(inp):
            cur = i%size
            if cur <= last:
                if len(rtn):
                    if isinstance(inp, str):
                        rtn[-1] = "".join(rtn[-1])
                    else:
                        rtn[-1] = type(inp)(rtn[-1])
                rtn.append([])
            rtn[-1].append(val)
            last = cur
        if len(rtn):
            if isinstance(inp, str):
                rtn[-1] = "".join(rtn[-1])
            else:
                rtn[-1] = type(inp)(rtn[-1])
        return [rtn]
    
    def split_space(self, inp:str):
        """return inp.split(" ")"""
        return self.split(inp, " ")
    
    @Node.test_func([3, 1], [3])
    @Node.test_func([3, 2], [2])
    @Node.test_func([7, 3], [6])
    def floor_remainder(self, a: Node.number, multiple: Node.number):
        """a-(a%multiple)"""
        return a - (a % multiple)
    
    @Node.test_func([[1, 2, 2, 3, 3, 3]], [{1: 1, 2: 2, 3: 3}])
    def count(self, seq: Node.sequence):
        """Return a dict with values equal to the number of times values appear in a list"""
        rtn = {}
        for i in seq:
            if i in rtn:
                rtn[i] += 1
            else:
                rtn[i] = 1
        return rtn

    @Node.test_func([3, "I"], [" I "])
    @Node.test_func([5, "It"], ["  It "])
    def center(self, length: int, string: str):
        """Center a `string` to `length`"""
        return string.center(length)

    def format_time(self, time_obj: Node.clock, string: str):
        return time.strftime(string, time_obj.time_obj)
