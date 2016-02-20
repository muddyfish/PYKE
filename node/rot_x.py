#!/usr/bin/env python

from nodes import Node
from node.numeric_literal import NumericLiteral 

class RotX(Node):
    char = "R"
    args = 0
    results = 0
    
    def __init__(self, amount):
        self.args = self.results = amount
        
    def prepare(self, stack):
        if self.args == 1:
            self.args = self.results = len(stack)
            
    def func(self, *args):
        return list(args[1:]+args[:1])
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, digits = NumericLiteral.accepts(code[1:])
            if new_code is None:
                digits = 2
                code = code[1:]
            else:
                digits = digits([])[0]
                code = new_code
            return code, cls(digits)
        return None, None