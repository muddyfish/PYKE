#!/usr/bin/env python

from nodes import Node

class Tail(Node):
    char = "t"
    args = 1
    results = 1
    
    @Node.test_func([2], [1])
    def sub_one(self, inp: Node.number):
        """inp-1"""
        return inp-1
    
    @Node.test_func([[1,2,3]], [[2,3]])
    def first(self, inp: Node.indexable):
        """inp[1:]"""
        return [inp[1:]]