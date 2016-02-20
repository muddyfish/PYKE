#!/usr/bin/env python

from nodes import Node

class Splice(Node):
    char = ":"
    args = 3
    results = 1
    
    def splice(self, a:Node.indexable, b:int, c:int):
        return a[b:c]
    
    def range(self, a:int, b:int, c:int):
        return [list(range(a,b,c))]
    
    def multi_assign(self, a:Node.indexable, b: Node.indexable, c: Node.indexable):
        for i in b:
            a[i] = c[i]
        return [a]
    
    def multi_assign_generic(self, a:Node.indexable, b: Node.indexable, c):
        for i in b:
            a[i] = c
        return [a]