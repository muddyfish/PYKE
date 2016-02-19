#!/usr/bin/env python

from nodes import Node
from node.base36_single import Base36Single 

class Join(Node):
    char = "]"
    args = 0
    results = 1
    
    def __init__(self, size):
        self.args = size
        
    def prepare(self, stack):
        if self.args == 0:
            self.args = len(stack)

    def func(self, *inp):
        return [inp]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, digits = Base36Single.accepts(code[1:], accept = True)
            if new_code is None:
                digits = 0
                code = code[1:]
            else:
                digits = digits([])[0]
                code = new_code
            return code, cls(digits)
        return None, None