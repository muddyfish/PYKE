#!/usr/bin/env python

from nodes import Node
from node.string_literal import StringLiteral 

class Join(Node):
    char = "J"
    args = 0
    results = 1
    
    def __init__(self, string):
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
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            code, string = StringLiteral.accepts('"'+code[1:])
            string = string([])[0]
            return code, cls(string)
        return None, None