#!/usr/bin/env python

from nodes import Node
from node.numeric_literal import NumericLiteral 

class RotX(Node):
    char = "R"
    args = 0
    results = 0
    default_arg = 2
    reverse_first = True
    
    def __init__(self, amount: Node.NumericLiteral):
        self.args = self.results = amount
        
    def prepare(self, stack):
        if self.args == 1:
            self.args = self.results = len(stack)
            
    def func(self, *args):
        args = args[::-1]
        return list(args[1:]+args[:1])
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.args)