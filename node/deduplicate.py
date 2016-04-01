#!/usr/bin/env python

from nodes import Node

class Deduplicate(Node):
    char = "}"
    args = 1
    results = 1
    
    @Node.test_func([2], [4])
    @Node.test_func([1.5], [3])
    def double(self, inp: Node.number):
        """inp*2"""
        return inp*2
        
    @Node.test_func([[1,2,3,1,1]], [[1,2,3]])
    @Node.test_func(["hi!!!"], ["hi!"])
    def func(self, seq:Node.indexable):
        """remove duplicates from seq"""
        seen = set()
        seen_add = seen.add
        if isinstance(seq, str):
            return "".join(x for x in seq if not (x in seen or seen_add(x)))
        return[type(seq)([x for x in seq if not (x in seen or seen_add(x))])]