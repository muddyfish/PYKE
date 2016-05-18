#!/usr/bin/env python

from nodes import Node
import copy

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
        rtn = []
        for _ in range(self.results):
            rtn.append(copy.deepcopy(a))
        return rtn
