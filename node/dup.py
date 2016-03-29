#!/usr/bin/env python

from nodes import Node

class Duplicate(Node):
    char = "D"
    args = 1
    results = 0
    default_arg = 2
    
    def __init__(self, amount: Node.NumericLiteral):
        self.results = amount
        
    @Node.test_func(["test"], ["test", "test"])  
    @Node.test_func([1], [1,1,1], "3")  
    def func(self, a):
        """Duplicate the top of the stack `amount` times"""
        return [a]*self.results
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.results)