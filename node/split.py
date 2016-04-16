#!/usr/bin/env python

from nodes import Node
from node.string_literal import StringLiteral 

class Split(Node):
    char = "c"
    args = 2
    results = 1
    
    @Node.test_func(["1 2 1", " "], [["1", "2", "1"]])
    @Node.test_func(["1,3,4", ","], [["1", "3", "4"]])
    def split(self, inp:str, split:str):
        """inp.split(`arg`)"""
        return [inp.split(split)]
    
    def chunk(self, inp:Node.indexable, size:Node.number):
        """Return inp seperated into groups sized size"""
        size = float(size)
        rtn = []
        last = 0
        for i, val in enumerate(inp):
            cur = i%size
            if cur <= last: rtn.append([])
            rtn[-1].append(val)
            last = cur
        return [rtn]
    
    def floor_remainder(self, a:Node.number, multiple:Node.number):
        """a-(a%multiple)"""
        return a-(a%multiple)
    