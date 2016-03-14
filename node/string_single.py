#!/usr/bin/env python

from nodes import Node

class StringLiteral(Node):
    args = 0
    results = 1
    char = "\\"

    def __init__(self, string):
        self.func = lambda: string

    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code):
        if code == "": return None, None
        if code[0] == '\\':
            string = code[1]
            code = code[2:]
            return code, cls(string)
        return None, None