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
        self.args = len(stack)
    
    def func(self, *inp):
        return self.string.join(map(str, inp))
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, string = StringLiteral.accepts('"'+code[1:])
            if new_code is None:
                string = ""
                code = code[1:]
            else:
                string = string([])[0]
                code = new_code
            return code, cls(string)
        return None, None