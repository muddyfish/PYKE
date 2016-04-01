#!/usr/bin/env python

from nodes import Node

import copy

class Variable(Node):
    char = ""
    args = 0
    results = 1
    ignore = True

    def func(self):
        return copy.deepcopy(self.__class__.contents)
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.__class__.contents)
        
    @classmethod
    def accepts(cls, code):
        if cls is Variable: return None, None
        if code[0] == cls.char:
            return code[1:], cls()
        return None, None