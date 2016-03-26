#!/usr/bin/env python

from nodes import Node

class Splice(Node):
    char = ":"
    args = 3
    results = 1
    
    def splice(self, a:Node.indexable, b:int, c:int):
        """a[b:c]"""
        return a[b:c]
    
    def range(self, a:int, b:int, c:int):
        """range(a,b,c)"""
        return [list(range(a,b,c))]
    
    def replace(self, a:str, b:str, c:str):
        """a.replace(b,c)"""
        return a.replace(b,c)
    
    def multi_assign(self, a:Node.indexable, b: Node.indexable, c: Node.indexable):
        """for i in b:
    a[i] = c[i]
return a"""
        for i in b:
            a[i] = c[i]
        return [a]
    
    def multi_assign_generic(self, a:Node.indexable, b: Node.indexable, c):
        """for i in b:
    a[i] = c
return a"""
        for i in b:
            a[i] = c
        return [a]