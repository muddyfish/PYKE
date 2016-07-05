#!/usr/bin/env python

from nodes import Node

class Index(Node):
    char = "@"
    args = 2
    results = 1
    
    @Node.test_func(["tes",1], ["e"])
    @Node.test_func([[1,2,3],-1], [3])
    def at(self, a: Node.indexable, b:int):
        """a[b]"""
        return[a[b]]
    
    
    @Node.test_func([2, {1:2,2:3}], [3])
    @Node.test_func(["hello", {"hello":"world"}], ["world"])
    @Node.prefer
    def dict_at(self, a, b:dict):
        return[b[a]]
    
    @Node.test_func([1, [1,2,3]], [0])
    @Node.test_func([3, [1,2,3]], [2])
    @Node.test_func([4, [1,2,3]], [-1])
    @Node.test_func(["e", "hello"], [1])
    @Node.test_func(["?", "hello"], [-1])
    @Node.prefer
    def index(self, a, b: Node.indexable):
        """b.index(a)"""
        if isinstance(b, str):
            return b.find(a)
        try:
            return b.index(a)
        except ValueError:
            return -1
    
    @Node.test_func([2, 0], [3])
    @Node.test_func([1, 2], [5])
    def set_bit(self, a: int, b: int):
        """Set bit b in a"""
        return a|(2**b)
    