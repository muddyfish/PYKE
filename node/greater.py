#!/usr/bin/env python

from nodes import Node

class Greater(Node):
    char = ">"
    args = 2
    results = 1
    
    @Node.test_func([4,2], [1])  
    @Node.test_func([0,0], [0])  
    @Node.test_func([4,5], [0])  
    def func(self, a,b):
        """a>b"""
        return (a>b)+0
    
    @Node.test_func(["test",2], ["st"])  
    def indexable_1(self, a:Node.indexable, b:int):
        """a[b:]"""
        return [a[b:]]
    
    @Node.test_func([3,"test"], ["est"])  
    def indexable_2(self, a:int, b:Node.indexable):
        """b[-a:]"""
        return [b[-a:]]
    