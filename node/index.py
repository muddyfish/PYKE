#!/usr/bin/env python

from nodes import Node

class Index(Node):
    char = "@"
    args = 2
    results = 1
    
    @Node.test_func(["tes",1], ["e"])
    @Node.test_func([[1,2,3],-1], [3])
    def at(self, a: Node.indexable, b: int):
        """a[b]"""
        return[a[b]]
    
    @Node.test_func([1,[1,2,3]], [0])
    @Node.test_func([3,[1,2,3]], [2])
    def index(self, a, b: Node.indexable):
        """b.index(a)"""
        return b.index(a)
    
    @Node.test_func([2, 0], [3])
    @Node.test_func([1, 2], [5])
    def set_bit(self, a: int, b: int):
        """Set bit b in a"""
        return a|(2**b)
    