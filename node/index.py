#!/usr/bin/env python

from nodes import Node

#At
@Node.test("@", [1,"tes"], ["e"])
@Node.test("@", [-1,[1,2,3]], [3])
#Index
@Node.test("@", [[1,2,3],1], [0])
@Node.test("@", [[1,2,3],3], [2])
#Set_bit
@Node.test("@", [0, 2], [3])
@Node.test("@", [2, 1], [5])
class Index(Node):
    char = "@"
    args = 2
    results = 1
    
    def at(self, a: Node.indexable, b: int):
        """a[b]"""
        return a[b]
    
    def index(self, a, b: Node.indexable):
        """b.index(a)"""
        return b.index(a)
    
    def set_bit(self, a: int, b: int):
        """Set bit b in a"""
        return a|(2**b)
    