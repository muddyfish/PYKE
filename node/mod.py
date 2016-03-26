#!/usr/bin/env python

from nodes import Node

#Modulo
@Node.test("%", [3,2], [2])
@Node.test("%", [5,6], [1])
#Every
@Node.test("%", [2, "testy"], ["tsy"])
@Node.test("%", [3, [1,2,3,4,5,6]], [[1,4]])
#Indexes
@Node.test("%", ["testy", "t"], [[0,3]])
@Node.test("%", [(1,0,1,2,1),1], [[0,2,4]])

class Mod(Node):
    char = "%"
    args = 2
    results = 1
    
    def modulo(self, a:Node.number,b:Node.number):
        """a%b"""
        return a%b
    
    def every(self, seq:Node.indexable, b:int):
        """seq[::b]"""
        return [seq[::b]]
    
    def indexes(self, a, b:Node.indexable):
        """Return a list of indecies in b that equal a"""
        return [list(i for i,v in enumerate(b) if v==a)]