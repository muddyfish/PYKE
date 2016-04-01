#!/usr/bin/env python

from nodes import Node

class Deduplicate(Node):
    char = "}"
    args = 1
    results = 2
    
    @Node.test_func([2], [4])
    @Node.test_func([1.5], [3])
    def double(self, inp: Node.number):
        """inp*2"""
        self.results = 1
        return inp*2
        
    def func(self, seq:Node.indexable):
        """remove duplicates from seq"""
        if isinstance(seq, str):
            return "".join(set(seq))
        return [type(seq)(set(seq))]