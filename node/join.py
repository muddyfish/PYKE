#!/usr/bin/env python

from nodes import Node

class Join(Node):
    char = "J"
    args = 0
    results = 1
    contents = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self, string: Node.StringLiteral):
        self.string = string
        
    def prepare(self, stack):
        if isinstance(stack[0], (list,tuple)):
            self.args = 1
        else:
            self.args = len(stack)
    
    @Node.test_func([1,5], ["15"])
    @Node.test_func([[1,5]], ["15"])
    @Node.test_func(["Hello", "World!"], ["Hello, World!"], ", ")
    @Node.test_func([1,2,3,4], ["1.2.3.4"], ".")
    def func(self, *inp):
        """If arg1 is a list or tuple, args = arg1
Else: args = stack.
return `fixed_arg`.join(args)"""
        if self.args == 1:
            inp = inp[0]
        return self.string.join(map(str, inp))
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
        