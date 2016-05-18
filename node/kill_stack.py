#!/usr/bin/env python

from nodes import Node

class KillStack(Node):
    char = ";"
    args = 0
    results = 0
    default_arg = 0
    
    def __init__(self, amount: Node.NumericLiteral):
        self.args = amount
        
    def prepare(self, stack):
        if self.args == 0:
            self.args = len(stack)
          
    @Node.test_func([4,2,4,5,1], [])  
    @Node.test_func([4,2], [], "2")  
    def func(self, *args):
        """Remove the first `amount` items from the stack"""
        return []
    