#!/usr/bin/env python

from nodes import Node

#Modulo
#Every
#Indexes

class Mod(Node):
    char = "%"
    args = 2
    results = 1
    
    @Node.test_func([2,3], [2])
    @Node.test_func([6,5], [1])
    def modulo(self, a:Node.number,b:Node.number):
        """a%b"""
        return a%b
    
    @Node.test_func(["testy",2], ["tsy"])
    @Node.test_func([[1,2,3,4,5,6],3], [[1,4]])
    def every(self, seq:Node.indexable, b:int):
        """seq[::b]"""
        return [seq[::b]]
    
    @Node.test_func(["t","testy"], [[0,3]])
    @Node.test_func([1,(1,0,1,2,1)], [[0,2,4]])
    def indexes(self, a, seq:Node.indexable):
        """Return a list of indecies in seq that equal a"""
        return [list(i for i,v in enumerate(seq) if v==a)]