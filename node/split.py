#!/usr/bin/env python

from nodes import Node
from node.string_literal import StringLiteral 

class Split(Node):
    char = "c"
    args = 1
    results = 1
    
    def __init__(self, string):
        self.string = string
    
    def func(self, inp):
        return [inp.split(self.string)]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            code, string = StringLiteral.accepts('"'+code[1:])
            string = string([])[0]
            if string == "": string = " "
            return code, cls(string)
        return None, None