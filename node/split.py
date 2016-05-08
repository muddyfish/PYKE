#!/usr/bin/env python

from nodes import Node
from node.string_literal import StringLiteral 

class Split(Node):
    char = "c"
    args = 2
    results = 1
    
    def prepare(self, stack):
        if len(stack) < 2:
            self.args = 1
    
    @Node.test_func(["1 2 1", " "], [["1", "2", "1"]])
    @Node.test_func(["1,3,4", ","], [["1", "3", "4"]])
    def split(self, inp:str, split:str):
        """inp.split(`arg`)"""
        return [inp.split(split)]
    
    @Node.test_func(["134", 1], [["1", "3", "4"]])
    @Node.test_func(["1234", 2], [["12", "34"]])
    def chunk(self, inp:Node.indexable, size:Node.number):
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
    
    def floor_remainder(self, a:Node.number, multiple:Node.number):
        """a-(a%multiple)"""
        return a-(a%multiple)
    