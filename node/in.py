#!/usr/bin/env python

from nodes import Node

#Unset bit
@Node.test("{", [1,1], [1])
@Node.test("{", [1,3], [1])
@Node.test("{", [2,5], [1])
@Node.test("{", [0,7], [6])
#In
@Node.test("{", [[6,2,1],6], [1])
@Node.test("{", [[6,2,1],3], [0])
class In(Node):
    char = "{"
    args = 2
    results = 1
    def func(self, a,b:Node.indexable):
        """a in b. returns an int"""
        return (a in b) + 0
    
    def unset_bit(self, a: int, b: int):
        """Unset bit b in a"""
        bit = 2**b
        if a&bit:
            return a^bit
        return a
    