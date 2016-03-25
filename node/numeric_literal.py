#!/usr/bin/env python
    
from nodes import Node

class NumericLiteral(Node):
    args = 0
    results = 1

    def __init__(self, digits):
        self.digits = digits
        
    def func(self):
        return self.digits

    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.digits)
        
    @classmethod
    def accepts(cls, code, ignore_zeros = False):
        if code == "": return None, None
        digits = ""
        while len(code) != 0 and \
              (code[0].isdigit() or code[0] == ".") and \
              (ignore_zeros or digits != "0"):
            digits += code[0]
            code = code[1:]
        if digits:
            if digits[0] == "0" and digits != "0":    
                return code, cls(digits)
            try:
                return code, cls(int(digits))
            except ValueError:
                return code, cls(float(digits))
        return None, None
    