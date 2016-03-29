#!/usr/bin/env python

from nodes import Node

class Base36Single(Node):
    char = ""
    args = 0
    results = 1
    ignore = True

    def __init__(self, value):
        self.value = value
        
    def func(self):
        return self.value

    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code, accept = False):
        if not accept: return None, None
        if code == "": return None, None
        try:
            value = int(code[0], 36)
        except ValueError: return None, None
        return code[1:], cls(value)
    