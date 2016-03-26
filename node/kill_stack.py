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
        if self.args == KillStack.default_arg:
            self.args = len(stack)
            
    def func(self, *args):
        """Remove the first `amount` items from the stack"""
        return []
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.args)