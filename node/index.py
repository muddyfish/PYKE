#!/usr/bin/env python

from nodes import Node

class Index(Node):
    char = "@"
    args = 2
    results = 1
    
    @Node.test_func([1,"tes"], ["e"])
    @Node.test_func([-1,[1,2,3]], [3])
    def at(self, a, b: Node.indexable):
        """b[a]"""
        return[b[a]]
    
    @Node.test_func([[1,2,3],1], [0])
    @Node.test_func([[1,2,3],3], [2])
    def index(self, a: Node.indexable, b: int):
        """a.index(b)"""
        return a.index(b)
    
    @Node.test_func([2, 0], [3])
    @Node.test_func([1, 2], [5])
    def set_bit(self, a: int, b: int):
        """Set bit b in a"""
        return a|(2**b)
    