#!/usr/bin/env python
    
from nodes import Node

class NumericLiteral(Node):
    args = 0
    results = 1

    def __init__(self, digits):
        self.func = lambda: digits

    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code):
        if code == "": return None, None
        digits = ""
        while len(code) != 0 and \
              code[0].isdigit() and \
              digits != "0":
            digits += code[0]
            code = code[1:]
        if digits:
            return code, cls(int(digits))
        return None, None
    