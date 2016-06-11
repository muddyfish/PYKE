#!/usr/bin/env python

from nodes import Node

class Index(Node):
    char = "@"
    args = 2
    results = 1
    
    @Node.test_func([1,"tes"], ["e"])
    @Node.test_func([-1,[1,2,3]], [3])
    def at(self, a:int, b: Node.indexable):
        """b[a]"""
        return[b[a]]
    
    
    @Node.test_func([2, {1:2,2:3}], [3])
    @Node.test_func(["hello", {"hello":"world"}], ["world"])
    @Node.prefer
    def dict_at(self, a, b:dict):
        return[b[a]]
    
    @Node.test_func([[1,2,3],1], [0])
    @Node.test_func([[1,2,3],3], [2])
    @Node.test_func(["hello","e"], [1])
    @Node.test_func(["hello","?"], [-1])
    @Node.prefer
    def index(self, a: Node.indexable, b):
        """a.index(b)"""
        if isinstance(a, str):
            return a.find(b)
        return a.index(b)
    
    @Node.test_func([2, 0], [3])
    @Node.test_func([1, 2], [5])
    def set_bit(self, a: int, b: int):
        """Set bit b in a"""
        return a|(2**b)
    