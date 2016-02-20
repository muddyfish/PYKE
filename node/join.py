#!/usr/bin/env python

from nodes import Node

class Join(Node):
    char = "J"
    args = 0
    results = 1
    
    def __init__(self, string: Node.StringLiteral):
        self.string = string
        
    def prepare(self, stack):
        if isinstance(stack[0], list) or \
           isinstance(stack[0], tuple):
            self.args = 1
        else:
            self.args = len(stack)
    
    def func(self, *inp):
        if self.args == 1:
            inp = inp[0]
        return self.string.join(map(str, inp))
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
        