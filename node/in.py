#!/usr/bin/env python

from nodes import Node

class In(Node):
    char = "{"
    args = 2
    results = 1
    
    @Node.test_func([6,[6,2,1]], [1])
    @Node.test_func([3,[6,2,1]], [0])
    def func(self, a,b:Node.indexable):
        """a in b. returns an int"""
        return (a in b) + 0
    
    @Node.test_func([1,1], [1])
    @Node.test_func([3,1], [1])
    @Node.test_func([5,2], [1])
    @Node.test_func([7,0], [6])
    def unset_bit(self, a: int, b: int):
        """Unset bit b in a"""
        bit = 2**b
        if a&bit:
            return a^bit
        return a