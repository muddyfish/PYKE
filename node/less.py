#!/usr/bin/env python

from nodes import Node

class Equals(Node):
    char = "<"
    args = 2
    results = 1
    def func(self, a,b):
        """a<b"""
        return a<b
    
    def indexable_1(self, a:Node.indexable, b:int):
        """a[:b]"""
        return a[:b]
    
    def indexable_2(self, a:int, b:Node.indexable):
        """b[:len(b)-a]"""
        return b[:len(b)-a]
    