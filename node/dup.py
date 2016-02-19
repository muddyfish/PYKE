#!/usr/bin/env python

from nodes import Node

class Duplicate(Node):
    char = "D"
    args = 1
    results = 0
    
    def __init__(self, amount):
        self.results = amount
        
    def func(self, a):
        return [a]*self.results
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.results)
        
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