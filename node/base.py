#!/usr/bin/env python

from nodes import Node
from node.numeric_literal import NumericLiteral

class Base(Node):
    char = "b"
    args = 1
    results = 1
    contents = "0123456789abcdefghijklmnopqrstuvwxyz"
    
    def __init__(self, base):
        self.base = base
        
    def func(self, a):
        if isinstance(a, basestring):
            #Convert to int
            return int(a, self.base)
        elif isinstance(a, list) or\
             isinstance(a, tuple):
            #Convert to int
            result = 0
            for i, value in enumerate(a):
                result += value*(self.base**i)
            return result
        elif isinstance(a, int):
            #Convert to string
            if a == 0: return self.contents[0]
            sign = "-"*(a<0)
            a = abs(a)
            digits = []
            while a:
                digits.append(self.contents[a % self.base])
                a /= self.base
            return sign+''.join(digits[::-1])
        else:
            raise TypeError("%r cannot be converted between bases")
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.base)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, digits = NumericLiteral.accepts(code[1:])
            if new_code is None:
                digits = 10
                code = code[1:]
            else:
                digits = digits([])[0]
                code = new_code
            return code, cls(digits)
        return None, None