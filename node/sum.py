#!/usr/bin/env python

from nodes import Node

class Sum(Node):
    char = "s"
    args = 0
    results = 1
    default_arg = None
    
    def __init__(self, args: Node.Base10Single):
        if args == 0:
            args = 10
        self.args = args
        
    def prepare(self, stack):
        if self.args == Sum.default_arg:
            if isinstance(stack[0], list) or \
               isinstance(stack[0], tuple):
                self.args = 1
            else:
                self.args = len(stack)
    
    def func(self, *inp):
        if self.args == 1:
            inp = inp[0]
        if str in map(type, inp):
            inp = [str(i)for i in inp]
        current = inp[0]
        for val in inp[1:]:
            current += val
        return current
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        