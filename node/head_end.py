#!/usr/bin/env python

from nodes import Node

class HeadEnd(Node):
    char = "}"
    args = 1
    results = 2
    
    @Node.test_func([2], [4])
    @Node.test_func([1.5], [3])
    def double(self, inp: Node.number):
        """inp*2"""
        self.results = 1
        return inp*2
        
    @Node.test_func(["hello!"], ["h","!"])
    @Node.test_func([[1,2,3]], [1,3])
    def head_end(self, inp:Node.indexable):
        """inp[0], inp[-1]"""
        return [inp[0], inp[-1]]