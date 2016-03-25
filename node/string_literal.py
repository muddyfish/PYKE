#!/usr/bin/env python

from nodes import Node

class StringLiteral(Node):
    args = 0
    results = 1
    char = '"'

    def __init__(self, string):
        self.string = string

    def func(self):
        return self.string

    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
        
    @classmethod
    def accepts(cls, code):
        if code == "": return None, None
        string = None
        if code[0] == '"':
            string = ""
            if len(code) != 1: 
                code = code[1:]
                while len(code) != 0 and code[0] != '"':
                    string += code[0]
                    code = code[1:]
            if len(code) != 0: code = code[1:]
        if string is not None:
            return code, cls(string)
        return None, None