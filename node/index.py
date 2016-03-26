#!/usr/bin/env python

from nodes import Node

class Index(Node):
    char = "@"
    args = 2
    results = 1
    
    def at(self, a: Node.indexable, b: int):
        """a[b]"""
        return a[b]
    
    def index(self, a: Node.indexable, b):
        """a.index(b)"""
        return a.index(b)
    
    def set_bit(self, a: int, b: int):
        """Set bit b in a"""
        return a|(2**b)
    